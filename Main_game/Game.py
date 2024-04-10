import pygame as pg
from Main_game.Setting import *
from Main_game.weapon import Weapon, Bullet
from gui.element import Element
from Main_game.Enemy import EnemiesManager
from Main_game.Timer import Timer

class Game(Element):
    def __init__(self):
        Element.__init__(self)
        self.running = True
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.weapon = Weapon()
        self.all_bullets = pg.sprite.Group()
        self.last_shot_time = 0
        self.enemies_manager = EnemiesManager() 
        self.timer = Timer() 
        
    def draw_map(self):
        self.img(650, 370, 1300, 900, "sprite/background_game.jpg")

    def handle_enemy_collision(self):
        for enemy in self.enemies_manager.enemies:
            hits = pg.sprite.spritecollide(enemy, self.all_bullets, True)
            for hit in hits:
                enemy.take_hit() 
                
    def handle_events(self):
        current_time = pg.time.get_ticks()  
        if current_time - self.last_shot_time >= 350:  # 350 millisecondes
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.weapon.shoot(self.all_bullets)  
                        self.last_shot_time = pg.time.get_ticks()  
                elif event.type == self.timer.timer_event:
                    self.timer.update()
                self.draw()
                pg.display.flip()
                self.clock.tick(30)



    def update_shooter(self):
        self.weapon.move()  
        for bullet in self.all_bullets:
            bullet.update()
        self.enemies_manager.update()
        self.handle_enemy_collision() 

    def draw(self):
        self.display.fill((0, 0, 0))  
        font = pg.font.Font(None, 36)
        self.draw_map()
        self.display.blit(self.weapon.asset, self.weapon.rect)  
        time_text = font.render(f"{self.timer.get_time()}", True, (255, 255, 255))
        text_rect = time_text.get_rect()
        text_rect.topright = (780, 20)  # Position en haut à droite
        self.display.blit(time_text, text_rect)


       
        for bullet in self.all_bullets:
            self.display.blit(bullet.bullet_canon, bullet.rect) 
        
        # Dessine chaque ennemi
        for enemy in self.enemies_manager.enemies:
            
            flipped_image = pg.transform.flip(enemy.image, True, False)  # Inverse l'image de l'ennemi
            self.display.blit(flipped_image, enemy.rect)  # Dessine l'image inversée de l'ennemi à l'emplacement de son rect
            enemy.draw_health_bar(self.display)  # Dessine la barre de vie au-dessus de l'ennemi


    def run(self):
        while self.running:
            self.handle_events()
            self.weapon.update()
            self.update_shooter()
            self.enemies_manager.spawn_enemy()  # Appel pour faire apparaître les ennemis
            self.draw()
            pg.display.flip()  # Met à jour l'affichage
            self.clock.tick(FPS)