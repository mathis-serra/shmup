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
        self.weapon = Weapon()
        self.all_bullets = pg.sprite.Group()
        self.last_shot_time = 0
        
    def draw_map(self):
        self.img(650, 370, 1300, 900, "sprite/background_game.jpg")

    def handle_events(self):
        current_time = pg.time.get_ticks()  # Récupère le temps actuel
        # Vérifie si suffisamment de temps s'est écoulé depuis le dernier tir
        if current_time - self.last_shot_time >= 350:  # 350 millisecondes
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE: 
                        if self.weapon.shoot(self.all_bullets):
                            self.last_shot_time = pg.time.get_ticks()  # Met à jour le dernier temps de tir
                            self.weapon.update(self.all_bullets)  # Réinitialise l'image après un délai


    def update_shooter(self):
        self.weapon.move()  # Déplace l'arme
        for bullet in self.all_bullets:
            bullet.update()  # Met à jour la position de chaque balle

    def draw(self):
        self.display.fill((0, 0, 0))
        self.draw_map()
        self.display.blit(self.weapon.asset, self.weapon.rect)
        # Dessine chaque balle
        for bullet in self.all_bullets:
            self.display.blit(bullet.bullet_canon, bullet.rect)            

    def run(self):
        while self.running:
            self.handle_events()
            self.update_shooter()
            self.draw()
            self.update()
            self.clock.tick(FPS)
        
