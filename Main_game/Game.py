import pygame as pg
from Main_game.Setting import *
from Main_game.weapon import Weapon, Bullet


class Game:
    def __init__(self):
        self.running = True
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.weapon = Weapon()  # Create an instance of Weapon
        self.all_bullets = pg.sprite.Group()  # Using pygame sprite group for bullets
        self.last_shot_time = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.weapon.shoot(self.all_bullets)  # Pass all_bullets group to shoot method
                    self.last_shot_time = pg.time.get_ticks()  # Update the last shot time

    def update(self):
        self.weapon.move()  # Move the weapon
        self.all_bullets.update()  # Update all bullets

    def draw(self):
        self.display.fill((0, 0, 0))  # Fill the screen with black color
        self.display.blit(self.weapon.image, self.weapon.rect)  # Draw the weapon's image
        self.all_bullets.draw(self.display)  # Draw all bullets
        pg.display.flip()  # Update the display

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
