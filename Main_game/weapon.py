import pygame as pg
from Main_game.Setting import *

# Dans weapon.py
class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loaded_cannon = pg.image.load(f'assets/sprite/canon_charger.png')  # Chargement de l'image du canon
        self.loaded_cannon = pg.transform.scale(self.loaded_cannon, (150, 85))  # Redimensionner l'image
        self.fired_cannon = pg.image.load(f'assets/sprite/canon_shooting.png')  # Charge l'image du canon après le tir
        self.fired_cannon = pg.transform.scale(self.fired_cannon, (210, 100))  # Redimensionner l'image
        self.asset = self.loaded_cannon
        self.rect = self.asset.get_rect(center=(WIDTH / 2 - 580, HEIGHT / 2))

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.rect.y -= 5
        elif keys[pg.K_s]:
            self.rect.y += 5
            
        # Limit the movement to stay within the screen boundaries
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))


    def shoot(self, bullets_group):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)
        self.asset = self.fired_cannon  # Change l'image du canon après le tir
        pg.time.set_timer(pg.USEREVENT + 1, 500)   # Déclenche un événement pour réinitialiser l'image après 500 millisecondes

    def reset_image(self):
        self.image = self.loaded_cannon 


# Dans bullet.py
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.bullet_canon = pg.image.load(f'assets/sprite/boule_canon.png')
        self.bullet_canon= pg.transform.scale(self.bullet_canon, (30, 30)) # Charge l'image de la balle
        self.rect = self.bullet_canon.get_rect(center=(x+70, y+17))
        self.speed = +10  # Bullet speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Supprime la balle si elle sort de l'écra
