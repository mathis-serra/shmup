import pygame as pg
import random
from Main_game.Setting import WIDTH, HEIGHT
from Main_game.weapon import Weapon

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation_frames = []
        for i in range(7):  # Assurez-vous d'adapter la boucle pour couvrir toutes les images
            frame = pg.image.load(f"assets/PNG/1/1_entity_000_walk_00{i}.png").convert_alpha()
            frame = pg.transform.scale(frame, (90, 90))  # Redimensionnez si nécessaire
            self.animation_frames.append(frame)
            # self.image = pg.transform.flip(self.image, True, False)  # Reverse the image horizontally
        self.frame_index = 0  # Indice du cadre actuel
        self.image = self.animation_frames[self.frame_index]  # Image actuelle de l'ennemi
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH  # Apparition à droite de l'écran
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.hit_count = 0  # Nombre de coups reçus
        self.kill_count = 0
        self.max_hit_count = 2  # Nombre maximum de coups avant la destruction de l'ennemi
        self.animation_speed = 0.2  # Vitesse de l'animation (en secondes)
        self.last_update = pg.time.get_ticks()  # Dernière mise à jour de l'animation

    def update(self):
        self.rect.x -= 1  # Déplacement vers la gauche
        if self.rect.right < 0:
            self.kill()  # Supprime l'ennemi carré s'il sort de l'écran           
            
        current_time = pg.time.get_ticks()
        if current_time - self.last_update > self.animation_speed * 1000:  # Convertir en millisecondes
            self.last_update = current_time
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames)  # Boucle à travers les images
            self.image = self.animation_frames[self.frame_index]  # Mettre à jour l'image affichée

    def take_hit(self):
        self.hit_count += 1
        if self.hit_count >= self.max_hit_count:  # Si l'ennemi a été touché le nombre maximum de fois
            self.kill()  # Détruire l'ennemi
            return True
        return False

    def draw_health_bar(self, surface):
        bar_width = self.rect.width
        bar_height = 5
        bar_x = self.rect.x
        bar_y = self.rect.y - 10
        remaining_hits = self.max_hit_count - self.hit_count
        fill_width = bar_width * remaining_hits / self.max_hit_count
        outline_rect = pg.Rect(bar_x, bar_y, bar_width, bar_height)
        fill_rect = pg.Rect(bar_x, bar_y, fill_width, bar_height)
        pg.draw.rect(surface, (0, 255, 0), fill_rect)  
        pg.draw.rect(surface, (255, 255, 255), outline_rect, 2)  
        
        
        
        
        
        
class EnemyHigh(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/sprite/Pirate-boat.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (200, 100))  # Redimensionner l'image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0, HEIGHT // 2 - self.rect.height)
        self.hit_count = 0
        self.max_hit_count = 2
        self.animation_speed = 0.2
        self.last_update = pg.time.get_ticks()

    def update(self):
        self.rect.x -= 1
        if self.rect.right < 0:
            self.kill()

        current_time = pg.time.get_ticks()
        if current_time - self.last_update > self.animation_speed * 1000:
            self.last_update = current_time

    def take_hit(self):
        self.hit_count += 1
        if self.hit_count >= 10:  # Le bateau pirate prend 5 coups avant d'être détruit
            self.kill()  # Détruire le bateau pirate
            return True
        return False

            
    def draw_health_bar(self, surface):
        bar_width = self.rect.width
        bar_height = 5
        bar_x = self.rect.x
        bar_y = self.rect.y - 10
        remaining_hits = 5 - self.hit_count  # Calcul du nombre de coups restants
        fill_width = bar_width * remaining_hits / 5  # Utilisation de 5 comme nombre total de coups
        fill_rect = pg.Rect(bar_x, bar_y, fill_width, bar_height)
        outline_rect = pg.Rect(bar_x, bar_y, bar_width, bar_height)
        pg.draw.rect(surface, (0, 255, 0), fill_rect)  # Dessine la partie remplie de la barre de vie
        pg.draw.rect(surface, (255, 255, 255), outline_rect, 2)  # Dessine le contour de la barre de vie

                

class EnemiesManager:
    def __init__(self):
        self.enemies = pg.sprite.Group()
        self.last_enemy_time = 0
        self.last_high_enemy_time = 0  # Ajoutez une nouvelle variable pour suivre le temps du dernier ennemi haut

    def create_enemy(self):
        enemy = Enemy() 
        enemy.rect.y = random.randint(HEIGHT // 2, HEIGHT - enemy.rect.height)
        self.enemies.add(enemy)

    def create_high_enemy(self):
        enemy_high = EnemyHigh()  # Créez un nouvel ennemi haut
        self.enemies.add(enemy_high)

    def update(self):
        self.enemies.update()

    def spawn_enemy(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_enemy_time > 2000:  
            self.create_enemy()
            self.last_enemy_time = current_time

        if current_time - self.last_high_enemy_time > 30000:  # Créez un nouvel ennemi haut toutes les vingts secondes
            self.create_high_enemy()
            self.last_high_enemy_time = current_time

        for enemy in self.enemies:
            enemy.update()

    def handle_collisions(self, bullets_group):
        collisions = pg.sprite.groupcollide(self.enemies, bullets_group, False, True)
        for enemy, bullets in collisions.items():
            for bullet in bullets:
                enemy.take_hit()      