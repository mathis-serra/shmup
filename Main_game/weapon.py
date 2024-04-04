import pygame as pg
from Main_game.Setting import *


class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))  # Example surface for weapon image
        self.image.fill((255, 255, 255))  # White rectangle as placeholder
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        elif keys[pg.K_RIGHT]:
            self.rect.x += 5

    def shoot(self, bullets_group):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)


# Dans weapon.py
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((10, 10))  # Example surface for bullet image
        self.image.fill((255, 0, 0))  # Red circle as placeholder
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10  # Bullet speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove the bullet if it goes off-screen