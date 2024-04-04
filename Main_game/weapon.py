import pygame as pg
from Main_game.Setting import *


class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))  # Example surface for weapon image
        self.image.fill((255, 255, 255))  # White rectangle as placeholder
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def shoot(self, bullets_group):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)
    

    def move(self):
        keys = pg.key.get_pressed()

        # Check left movement
        if keys[pg.K_q] and self.rect.left > 0:
            self.rect.x -= 5
        # Check right movement
        if keys[pg.K_d] and self.rect.right < WIDTH:
            self.rect.x += 5

    def collide(self):
        if self.rect.left < 0 or self.rect.right > WIDTH:
            return True
        return False

    
    
    
    # def __init__(self, x, y):
    #     self.radius = 5  # Set the radius of the bullet
    #     self.color = (0, 255, 0)  # Set the color of the bullet
    #     self.rect = pg.Rect(0, 0, self.radius * 2, self.radius * 2)
    #     self.rect.center = (x, y)  # Set the initial position of the bullet
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