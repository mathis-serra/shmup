import pygame as pg
# import json
from Main_game.Setting import *
from Main_game.weapon import Weapon, Bullet
from gui.element import Element
from Main_game.Enemy import EnemiesManager, EnemyHigh
from Main_game.Timer import Timer
from Main_game.Enemy import Enemy

class Game(Element):
    def __init__(self):
        Element.__init__(self)
        self.running = True
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.weapon = Weapon()
        self.timer = Timer()
        self.all_bullets = pg.sprite.Group()
        self.last_shot_time = 0
        self.enemies_manager = EnemiesManager()
        self.x_limit = 80
        self.end_screen = False
        self.hall_of_hame = False
        self.enemy = Enemy()
        self.score = 0
        
    def draw_map(self):
        self.img(650, 370, 1300, 900, "sprite/background_game.jpg")

    def handle_enemy_collision(self):
        for enemy in self.enemies_manager.enemies:
            hits = pg.sprite.spritecollide(enemy, self.all_bullets, True)
            for hit in hits:
                if enemy.take_hit():  
                    if isinstance(enemy, EnemyHigh):
                        self.score += 5
                    else:
                        self.score += 2
                
    def handle_events(self):
        current_time = pg.time.get_ticks()  
        if current_time - self.last_shot_time >= 350:  
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE: 
                        self.weapon.shoot(self.all_bullets)  
                        self.last_shot_time = pg.time.get_ticks()
                    elif event.key == pg.K_RETURN :
                        if self.end_screen or self.hall_of_hame:
                            self.running = False
                    elif event.key == pg.K_TAB:
                        if self.end_screen:
                            self.hall_of_hame = True 

    def update_shooter(self):
        self.weapon.move()  
        for bullet in self.all_bullets:
            bullet.update()
        self.enemies_manager.update()
        self.handle_enemy_collision()

        for enemy in self.enemies_manager.enemies:
            if enemy.rect.right <= self.x_limit:
                self.weapon.health -= 50  
                enemy.rect.x = WIDTH  
                self.weapon.health = max(0, self.weapon.health)

        if self.weapon.health <= 0:
            self.end_screen = True        
         

    def draw(self):
        self.display.fill((0, 0, 0))
        self.draw_map()
        self.display.blit(self.weapon.asset, self.weapon.rect)  

        for bullet in self.all_bullets:
            self.display.blit(bullet.bullet_canon, bullet.rect)  
            
        for enemy in self.enemies_manager.enemies:
            flipped_image = pg.transform.flip(enemy.image, True, False)  
            self.display.blit(flipped_image, enemy.rect)  
            enemy.draw_health_bar(self.display)  
            self.weapon.health_bar(self.display)
            
        font = pg.font.Font(None, 60)
        time_text = font.render(self.timer.get_time(), True, self.white)
        self.display.blit(time_text, (550, 10))        
        
        font = pg.font.Font(None, 50)
        score_text = font.render(f"Score: {self.score}", True, self.white)
        self.display.blit(score_text, (10, 650))
                    
    def game_over(self):
        self.handle_enemy_collision()

        if self.end_screen:
            self.img(650, 370, 1300, 750, "menu/background_menu.png")
            self.img(630, 140, 320, 110, "menu/logo_game.png")
            self.text(60, "GAME OVER", self.dark_red, 480, 300)
            self.text(43, "PRESS ENTER TO RETURN MENU", self.black, 370, 400)
            font = pg.font.Font(None, 43)
            score_text = font.render(f"Votre score est de : {str(self.score)} points", True, self.black)
            self.display.blit(score_text, (425, 500))
    
                    
        # self.save_score()  # Enregistrer le score lorsque la partie est terminée
        # self.load_scores()  # Charger les scores à partir du fichier JSON
        # self.display_hall_of_hame()

    # def display_hall_of_hame(self):
    #     if self.hall_of_hame:
    #         if self.scores:
    #             hall_of_fame_y = (HEIGHT - len(self.scores) * 30 - 40) / 2
    #             self.text(40, "Hall of Fame:", self.black, 530, hall_of_fame_y)
    #             for i, score_data in enumerate(self.scores, start=1):
    #                 score = score_data['score']
    #                 self.text(30, f"Partie {score_data['id']}: {score}", self.black, 530, hall_of_fame_y + 40 + i * 30)  
                    
    # def save_score(self):
    #     try:
    #         with open('scores.json', 'r') as file:
    #             previous_scores = json.load(file)
    #     except FileNotFoundError:
    #         previous_scores = {'parties': []}

    #     self.scores.append({'id': len(previous_scores['parties']) + 1, 'score': self.score})
    #     previous_scores['parties'].extend(self.scores)

    #     with open('scores.json', 'w') as file:
    #         json.dump(previous_scores, file)

            
    # def load_scores(self):
    #     try:
    #         with open("scores.json", "r") as file:
    #             scores_data = json.load(file)
    #             self.scores = scores_data.get('parties', [])
    #     except FileNotFoundError:
    #         self.scores = []


    def run(self):
        while self.running:
            super().update()
            self.handle_events()
            self.weapon.update()
            self.update_shooter()
            self.enemies_manager.spawn_enemy()  
            self.draw()  

            if self.end_screen:
                self.game_over()

            self.timer.update()
            self.clock.tick(FPS)

