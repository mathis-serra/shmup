import pygame as pg
from Main_game.Setting import *

# In weapon.py
class Weapon(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loaded_cannon = pg.image.load(f'assets/sprite/canon_charger.png')
        self.loaded_cannon = pg.transform.scale(self.loaded_cannon, (150, 85))
        self.loaded_cannon_rect = self.loaded_cannon.get_rect(center=(WIDTH / 2 - 580, HEIGHT / 2))

        self.fired_cannon = pg.image.load(f'assets/sprite/canon_shooting.png')
        self.fired_cannon = pg.transform.scale(self.fired_cannon, (210, 102))
        self.fired_cannon_rect = self.fired_cannon.get_rect()  # Using an empty rect for now

        self.asset = self.loaded_cannon
        self.rect = self.loaded_cannon_rect
        self.shoot_time = 0
        self.shoot_duration = 60  # Duration of the shooting image in milliseconds

        # Adding manual offset to align the images
        self.offset_x = 33
        self.offset_y = -8
        
        self.health = 100
        self.max_health = 100
        # Health bar dimensions
        self.health_bar_length = 100
        self.health_bar_height = 10

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.y -= 5
        elif keys[pg.K_DOWN]:
            self.rect.y += 5

        # Limit the movement to stay within the screen boundaries
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def shoot(self, bullets_group):
        self.asset = self.fired_cannon
        self.rect = self.fired_cannon_rect
        # Update the position of the shooting image rect with manual offset
        self.fired_cannon_rect.center = (self.loaded_cannon_rect.center[0] + self.offset_x, 
                                          self.loaded_cannon_rect.center[1] + self.offset_y)  
        self.shoot_time = pg.time.get_ticks()  # Record the time of the shot

        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets_group.add(bullet)
        
    def health_bar(self, surface):
        # Calculate the width of the health bar based on health
        bar_width = int((self.health / self.max_health) * self.health_bar_length)
        # Determine the color of the health bar based on health
        if self.health > 50:
            bar_color = (0, 255, 0)  # Green
        elif 20 <= self.health <= 50:
            bar_color = (255, 255, 0)  # Yellow
        else:
            bar_color = (255, 0, 0)  # Red
        # Draw the health bar
        # Calculate the coordinates of the health bar to place it just above the weapon
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


# In bullet.py
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.bullet_canon = pg.image.load(f'assets/sprite/boule_canon.png')
        self.bullet_canon = pg.transform.scale(self.bullet_canon, (30, 30)) # Load the bullet image
        self.rect = self.bullet_canon.get_rect(center=(x+37, y+37))
        self.speed = +10  # Speed of the bullet

    def update(self):
        self.rect.x += self.speed
        if self.rect.bottom < 0:
            self.kill()  # If bullet is off-screen, remove it
