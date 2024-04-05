import pygame as pg
from Main_game.Setting import *
from Main_game.weapon import Weapon, Bullet
from gui.element import Element


class Game(Element):
    def __init__(self):
        Element.__init__(self)
        self.running = True
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.weapon = Weapon()  # Create an instance of Weapon
        self.all_bullets = pg.sprite.Group()  # Using pygame sprite group for bullets
        self.last_shot_time = 0



    def handle_events(self):
        current_time = pg.time.get_ticks()  # Get the current time
        # Check if enough time has passed since the last shot
        if current_time - self.last_shot_time >= 350:  # 350 milliseconds
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE: 
                        self.weapon.shoot(self.all_bullets)  # Pass all_bullets group to shoot method
                        self.last_shot_time = pg.time.get_ticks()  # Update the last shot time

    def update_shooter(self):
        self.weapon.move()  # Move the weapon
        for bullet in self.all_bullets:
            bullet.update()  # Update each bullet's position

    def draw(self):
        self.display.fill((0, 0, 0))  # Fill the screen with black color
        self.display.blit(self.weapon.image, self.weapon.rect)  # Draw the weapon's image
        self.all_bullets.draw(self.display)  # Draw all bullets
        self.update()  # Update the display

    def run(self):
        while self.running:
            self.handle_events()
            self.update_shooter()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()
