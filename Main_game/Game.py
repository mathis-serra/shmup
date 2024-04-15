import pygame as pg
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
                if enemy.take_hit():  # Vérifiez si l'ennemi est détruit et incrémentez le score en conséquence
                    if isinstance(enemy, EnemyHigh):
                        self.score += 5
                    else:
                        self.score += 2

 
                
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
                    elif event.key == pg.K_RETURN :
                        if self.end_screen or self.hall_of_hame:
                            self.running = False
                    # elif event.key == pg.K_TAB:
                    #     if self.end_screen:
                    #         self.hall_of_hame = True 


    def update_shooter(self):
        self.weapon.move()  
        for bullet in self.all_bullets:
            bullet.update()
        self.enemies_manager.update()
        self.handle_enemy_collision()

        # Vérifier si un ennemi a atteint la coordonnée X seuil
        for enemy in self.enemies_manager.enemies:
            if enemy.rect.right <= self.x_limit:
                self.weapon.health -= 50  # Réduire d'un point de vie
                # Réinitialiser la position de l'ennemi pour éviter de perdre plusieurs points de vie
                enemy.rect.x = WIDTH  # Réinitialiser la position de l'ennemi
                # Assurez-vous que le point de vie ne devienne pas négatif
                self.weapon.health = max(0, self.weapon.health)

        # Vérifier si le joueur est mort
        if self.weapon.health <= 0:
            # Gérer la défaite ou autre logique à exécuter lorsque le joueur est mort
            self.end_screen = True        
         

    def draw(self):
        self.display.fill((0, 0, 0))
        self.draw_map()
        self.display.blit(self.weapon.asset, self.weapon.rect)  # Dessine l'image de l'arme

        # Dessine chaque balle
        for bullet in self.all_bullets:
            self.display.blit(bullet.bullet_canon, bullet.rect)  # Dessine l'image de la balle à l'emplacement de son rect
            
        for enemy in self.enemies_manager.enemies:
            
            flipped_image = pg.transform.flip(enemy.image, True, False)  # Inverse l'image de l'ennemi
            self.display.blit(flipped_image, enemy.rect)  # Dessine l'image inversée de l'ennemi à l'emplacement de son rect
            enemy.draw_health_bar(self.display)  # Dessine la barre de vie au-dessus de l'ennemi
            self.weapon.health_bar(self.display)
            
        # Afficher le temps écoulé
        font = pg.font.Font(None, 60)
        time_text = font.render(self.timer.get_time(), True, self.white)
        self.display.blit(time_text, (550, 10))        
        
        # Afficher le score total du joueur
        font = pg.font.Font(None, 50)
        score_text = font.render(f"Score: {self.score}", True, self.white)
        self.display.blit(score_text, (10, 650))
                    
    def game_over(self):
        self.img(650, 370, 1300, 750, "menu/background_menu.png")
        self.img(630, 140, 320, 110, "menu/logo_game.png")
        self.text(60, "GAME OVER", self.dark_red, 480, 300)
        self.text(43, "PRESS ENTER TO RETURN MENU", self.black, 370, 400)
        self.text(40, f"Votre score est de : {self.enemy.kill_player}", self.black, 530, 500)
        # self.scores.append(self.enemy.kill_player)  # Ajoutez le score total des ennemis à la liste des scores
        
    # def display_hall_of_hame(self):
    #     self.img(650, 370, 1300, 750, "menu/background_home.jpg")
    #     for score in self.scores:
    #         self.text(30, f"Votre Score est de : {score}", self.black, 470, 320)              
        



    def run(self):
        while self.running:
            super().update()
            self.handle_events()
            self.weapon.update()
            self.update_shooter()
            self.enemies_manager.spawn_enemy()  # Appel pour faire apparaître les ennemis
            self.draw()
            if self.end_screen:
                self.game_over()
            # if self.hall_of_hame:
            #     self.display_hall_of_hame()
            self.timer.update()
            self.clock.tick(FPS)