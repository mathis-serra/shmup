import pygame as pg
import random
from Main_game.Setting import WIDTH, HEIGHT
from Main_game.weapon import Weapon

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animation_frames = []
        for i in range(7):  # Make sure to adjust the loop to cover all images
            frame = pg.image.load(f"assets/PNG/1/1_entity_000_walk_00{i}.png").convert_alpha()
            frame = pg.transform.scale(frame, (90, 90))  # Resize if necessary
            self.animation_frames.append(frame)
            # self.image = pg.transform.flip(self.image, True, False)  # Reverse the image horizontally
        self.frame_index = 0  # Index of the current frame
        self.image = self.animation_frames[self.frame_index]  # Current image of the enemy
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH  # Spawn on the right side of the screen
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.hit_count = 0  # Number of hits taken
        self.kill_count = 0
        self.max_hit_count = 2  # Maximum number of hits before enemy destruction
        self.animation_speed = 0.2  # Animation speed (in seconds)
        self.last_update = pg.time.get_ticks()  # Last animation update time

    def update(self):
        self.rect.x -= 2  # Move left
        if self.rect.right < 0:
            self.kill()  # Remove the square enemy if it goes off-screen

        current_time = pg.time.get_ticks()
        if current_time - self.last_update > self.animation_speed * 1000:  # Convert to milliseconds
            self.last_update = current_time
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames)  # Loop through the images
            self.image = self.animation_frames[self.frame_index]  # Update the displayed image

    def take_hit(self):
        self.hit_count += 1
        if self.hit_count >= self.max_hit_count:  # If the enemy has been hit the maximum number of times
            self.kill()  # Destroy the enemy
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
        self.image = pg.transform.scale(self.image, (200, 100))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0, HEIGHT // 2 - self.rect.height)
        self.hit_count = 0
        self.max_hit_count = 2
        self.animation_speed = 0.2
        self.last_update = pg.time.get_ticks()

    def update(self):
        self.rect.x -= 1.5
        if self.rect.right < 0:
            self.kill()

        current_time = pg.time.get_ticks()
        if current_time - self.last_update > self.animation_speed * 1000:
            self.last_update = current_time

    def take_hit(self):
        self.hit_count += 1
        if self.hit_count >= 10:  # The pirate boat takes 5 hits before being destroyed
            self.kill()  # Destroy the pirate boat
            return True
        return False

    def draw_health_bar(self, surface):
        bar_width = self.rect.width
        bar_height = 5
        bar_x = self.rect.x
        bar_y = self.rect.y - 10
        remaining_hits = 5 - self.hit_count  # Calculating remaining hits
        fill_width = bar_width * remaining_hits / 5  # Using 5 as total number of hits
        fill_rect = pg.Rect(bar_x, bar_y, fill_width, bar_height)
        outline_rect = pg.Rect(bar_x, bar_y, bar_width, bar_height)
        pg.draw.rect(surface, (0, 255, 0), fill_rect)  # Draw the filled part of the health bar
        pg.draw.rect(surface, (255, 255, 255), outline_rect, 2)  # Draw the outline of the health bar

class EnemiesManager:
    def __init__(self):
        self.enemies = pg.sprite.Group()
        self.last_enemy_time = 0
        self.last_high_enemy_time = 0  # Add a new variable to track the time of the last high enemy

    def create_enemy(self):
        enemy = Enemy() 
        enemy.rect.y = random.randint(HEIGHT // 2, HEIGHT - enemy.rect.height)
        self.enemies.add(enemy)

    def create_high_enemy(self):
        enemy_high = EnemyHigh()  # Create a new high enemy
        self.enemies.add(enemy_high)

    def update(self):
        self.enemies.update()

    def spawn_enemy(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_enemy_time > 2000:  
            self.create_enemy()
            self.last_enemy_time = current_time

        if current_time - self.last_high_enemy_time > 30000:  # Create a new high enemy every thirty seconds
            self.create_high_enemy()
            self.last_high_enemy_time = current_time

        for enemy in self.enemies:
            enemy.update()

    def handle_collisions(self, bullets_group):
        collisions = pg.sprite.groupcollide(self.enemies, bullets_group, False, True)
        for enemy, bullets in collisions.items():
            for bullet in bullets:
                enemy.take_hit() 
