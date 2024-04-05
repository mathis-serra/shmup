import pygame as pg
from Main_game.Setting import *

# Dans weapon.py
class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loaded_cannon = pg.image.load(f'assets/sprite/canon_charger.png')  # Chargement de l'image du canon
        self.loaded_cannon = pg.transform.scale(self.loaded_cannon, (150, 85))  # Redimensionner l'image
        self.rect = self.loaded_cannon.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        elif keys[pg.K_RIGHT]:
            self.rect.x += 5
        
        # Limiter le mouvement pour rester dans les limites de l'écran
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

    def shoot(self, bullets_group):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)


# Dans bullet.py
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.bullet_canon = pg.image.load(f'assets/sprite/boule_canon.png')
        self.bullet_canon= pg.transform.scale(self.bullet_canon, (30, 30)) # Charge l'image de la balle
        self.rect = self.bullet_canon.get_rect(center=(x, y))
        self.speed = -10  # Vitesse de la balle

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Supprime la balle si elle sort de l'écra
