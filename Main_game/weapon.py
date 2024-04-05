import pygame as pg
import pygame
from Main_game.Setting import *


# Dans weapon.py
class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loaded_cannon = pygame.image.load(f'assets/sprite/canon_charger.png')  # Example surface for weapon image
        self.loaded_cannon.fill((255, 255, 255))  # White rectangle as placeholder
        self.rect = self.loaded_cannon.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        # self.cannon_shooting = pygame.image.load(f'assets/sprite/canon_shooting.png')        

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        elif keys[pg.K_RIGHT]:
            self.rect.x += 5
        
        # Limit the movement to stay within the screen boundaries
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

    def shoot(self, bullets_group):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)


# Dans bullet.py
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.bullet_canon = pygame.image.load(f'assets/sprite/boule_canon.png') # Example surface for bullet image
        self.bullet_canon.fill((255, 0, 0))  # Red circle as placeholder
        self.rect = self.bullet_canon.get_rect(center=(x, y))
        self.speed = -10  # Bullet speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove the bullet if it goes off-screen