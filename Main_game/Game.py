import pygame as pg
from Main_game.Setting import *
from Main_game.weapon import Weapon, Bullet


class Game:
    def __init__(self):
        self.running = True
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.weapon = Weapon()  # Create an instance of Weapon
        self.all_bullets = []  # List to store all the bullets
        self.last_shot_time = 0
        
        
        
    def handle_events(self):
        current_time = pg.time.get_ticks()  # Get the current time
        # Check if enough time has passed since the last shot
        if current_time - self.last_shot_time >= 350:  # 200 milliseconds = 0.2 seconds
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        bullet = self.weapon.shoot()  # Call shoot method from the weapon
                        self.all_bullets.append(bullet)  # Add the bullet to the list
                        self.last_shot_time = current_time  # Update the last shot time

    def update(self):
        self.weapon.move()  # Move the weapon
        for bullet in self.all_bullets:
            bullet.update()  # Update each bullet's position

    def draw(self):
        self.display.fill((0, 0, 0))  # Fill the screen with black color
        pg.draw.rect(self.display, (255, 255, 255), self.weapon.rect)  # Draw the weapon's rectangle
        for bullet in self.all_bullets:
            pg.draw.circle(self.display, bullet.color, bullet.rect.center, bullet.radius)  # Draw the bullets
        pg.display.flip()  # Update the display

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pg.quit()