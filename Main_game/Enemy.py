import pygame as pg
import random
from Main_game.Setting import WIDTH, HEIGHT
from Main_game.weapon import Bullet

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 30))  # Définit la taille de l'ennemi carré
        self.image.fill((0, 0, 255))  # Couleur bleue pour l'ennemi carré
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH  # Apparition à droite de l'écran
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.hit_count = 0  # Nombre de coups reçus
        self.kill_count = 0
        self.max_hit_count = 2  # Nombre maximum de coups avant la destruction de l'ennemi

    def update(self):
        self.rect.x -= 1  # Déplacement vers la gauche
        if self.rect.right < 0:
            self.kill()  # Supprime l'ennemi carré s'il sort de l'écran

    def take_hit(self):
        self.hit_count += 1
        if self.hit_count >= self.max_hit_count:  # Si l'ennemi a été touché le nombre maximum de fois
            self.kill()  # Détruire l'ennemi

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

class EnemiesManager:
    def __init__(self):
        self.enemies = pg.sprite.Group()
        self.last_enemy_time = 0

    def create_enemy(self):
        enemy = Enemy() 
        self.enemies.add(enemy)

    def update(self):
        self.enemies.update()

    def spawn_enemy(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_enemy_time > 2000:  
            self.create_enemy()
            self.last_enemy_time = current_time

    def handle_collisions(self, bullets_group):
        collisions = pg.sprite.groupcollide(self.enemies, bullets_group, False, True)
        for enemy, bullets in collisions.items():
            for bullet in bullets:
                enemy.take_hit() 