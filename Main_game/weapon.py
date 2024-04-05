import pygame as pg
from Main_game.Setting import *


# Dans weapon.py
class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))  # Example surface for weapon image
        self.image.fill((255, 255, 255))  # White rectangle as placeholder
        self.rect = self.image.get_rect(center=(WIDTH / 2 - 600, HEIGHT / 2))

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_z]:
            self.rect.y -= 5
        elif keys[pg.K_w]:
            self.rect.y += 5
            
        # Limit the movement to stay within the screen boundaries
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))


    def shoot(self, bullets_group):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        bullets_group.add(bullet)


# Dans bullet.py
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((10, 10))  # Example surface for bullet image
        self.image.fill((255, 0, 0))  # Red circle as placeholder
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = +10  # Bullet speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove the bullet if it goes off-screen