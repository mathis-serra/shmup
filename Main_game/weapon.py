import pygame as pg
from Main_game.Setting import *

# Dans weapon.py
class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loaded_cannon = pg.image.load(f'assets/sprite/canon_charger.png')
        self.loaded_cannon = pg.transform.scale(self.loaded_cannon, (150, 85))
        self.loaded_cannon_rect = self.loaded_cannon.get_rect(center=(WIDTH / 2 - 580, HEIGHT / 2))

        self.fired_cannon = pg.image.load(f'assets/sprite/canon_shooting.png')
        self.fired_cannon = pg.transform.scale(self.fired_cannon, (210, 102))
        self.fired_cannon_rect = self.fired_cannon.get_rect()  # Utilisation d'un rect vide pour l'instant

        self.asset = self.loaded_cannon
        self.rect = self.loaded_cannon_rect
        self.shoot_time = 0
        self.shoot_duration = 60  # Durée de l'image de tir en millisecondes

        # Ajouter un décalage manuel pour aligner les images
        self.offset_x = 33
        self.offset_y = -8
        
        self.health = 100
        self.max_health = 100
        # Dimensions de la barre de vie
        self.health_bar_length = 100
        self.health_bar_height = 10

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.rect.y -= 5
        elif keys[pg.K_s]:
            self.rect.y += 5

        # Limit the movement to stay within the screen boundaries
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def shoot(self, bullets_group):
        self.asset = self.fired_cannon
        self.rect = self.fired_cannon_rect
        # Mettre à jour la position du rectangle de l'image de tir avec le décalage manuel
        self.fired_cannon_rect.center = (self.loaded_cannon_rect.center[0] + self.offset_x, 
                                          self.loaded_cannon_rect.center[1] + self.offset_y)  
        self.shoot_time = pg.time.get_ticks()  # Enregistre le temps du tir

        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)
        
    def health_bar(self, surface):
        # Calcule la largeur de la barre de vie en fonction de la santé
        bar_width = int((self.health / self.max_health) * self.health_bar_length)
        # Détermine la couleur de la barre de vie en fonction de la santé
        if self.health > 50:
            bar_color = (0, 255, 0)  # Vert
        elif 20 <= self.health <= 50:
            bar_color = (255, 255, 0)  # Jaune
        else:
            bar_color = (255, 0, 0)  # Rouge
        # Dessine la barre de vie
        # Calcule les coordonnées de la barre de vie pour la placer juste au-dessus de l'arme
        bar_x = self.rect.centerx - bar_width // 2
        bar_y = self.rect.top - self.health_bar_height
        pg.draw.rect(surface, bar_color, [bar_x, bar_y, bar_width, self.health_bar_height])
                

    def update(self):
        current_time = pg.time.get_ticks()
        if current_time - self.shoot_time > self.shoot_duration:
            self.reset_image()

    def reset_image(self):
        self.asset = self.loaded_cannon
        self.rect = self.loaded_cannon_rect 


# Dans bullet.py
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.bullet_canon = pg.image.load(f'assets/sprite/boule_canon.png')
        self.bullet_canon = pg.transform.scale(self.bullet_canon, (30, 30)) # Charge l'image de la balle
        self.rect = self.bullet_canon.get_rect(center=(x+37, y+37))
        self.speed = +10  # Vitesse de la balle

    def update(self):
        self.rect.x += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Si la balle est hors de l'écran, supprimez-la
