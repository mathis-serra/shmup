import pygame as pg
from Main_game.Setting import *


class Weapon:
    def __init__(self):
        self.radius = 10  # Set the radius of the rectangle
        self.rect = pg.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = (WIDTH // 2, HEIGHT - 50)  # Set the initial position of the rectangle 
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)  # Create a bullet object at the top center of the rectangle
        return bullet
        
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
    
    

class Bullet:
    def __init__(self, x, y):
        self.radius = 5  # Set the radius of the bullet
        self.color = (0, 255, 0)  # Set the color of the bullet
        self.rect = pg.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = (x, y)  # Set the initial position of the bullet

    def update(self):
        self.rect.y -= 5  # Move the bullet upwards with a slower speed
        if self.rect.bottom < 0:  # Remove the bullet when it goes off the screen
            return True
        return False