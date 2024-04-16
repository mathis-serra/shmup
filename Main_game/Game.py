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
        self.running = True  # Flag to control game loop
        self.display = pg.display.set_mode((WIDTH, HEIGHT))  # Set game display window size
        self.clock = pg.time.Clock()  # Create a clock object to control frame rate
        self.weapon = Weapon()  # Initialize player weapon
        self.timer = Timer()  # Initialize game timer
        self.all_bullets = pg.sprite.Group()  # Group for all bullets in the game
        self.last_shot_time = 0  # Keep track of the last time a bullet was shot
        self.enemies_manager = EnemiesManager()  # Initialize the enemies manager
        self.x_limit = 80  # X-coordinate limit for enemy spawn
        self.end_screen = False  # Flag to indicate if the game is over
        self.hall_of_hame = False  # Flag to indicate if the player is in the hall of fame
        self.enemy = Enemy()  # Initialize a single enemy (unused)
        self.score = 0  # Player's score

    def draw_map(self):
        """Draw the game map."""
        self.img(650, 370, 1300, 900, "sprite/background_game.jpg")

    def handle_enemy_collision(self):
        """Handle collisions between bullets and enemies."""
        for enemy in self.enemies_manager.enemies:
            hits = pg.sprite.spritecollide(enemy, self.all_bullets, True)
            for hit in hits:
                if enemy.take_hit():  
                    if isinstance(enemy, EnemyHigh):
                        self.score += 5
                    else:
                        self.score += 2
                
    def handle_events(self):
        """Handle user input events."""
        current_time = pg.time.get_ticks()  
        if current_time - self.last_shot_time >= 500:  
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
        """Update player-related entities."""
        self.weapon.move()  # Move the player weapon
        for bullet in self.all_bullets:
            bullet.update()  # Update bullet positions
        self.enemies_manager.update()  # Update enemy positions and behaviors
        self.handle_enemy_collision()  # Handle collisions between bullets and enemies

        for enemy in self.enemies_manager.enemies:
            if enemy.rect.right <= self.x_limit:
                self.weapon.health -= 50  # Decrease player health when enemy passes x limit
                enemy.rect.x = WIDTH  # Reset enemy position
                self.weapon.health = max(0, self.weapon.health)  # Ensure health doesn't go below 0

        if self.weapon.health <= 0:
            self.end_screen = True  # Activate game over screen if player health reaches 0

    def draw(self):
        """Draw game elements on the screen."""
        self.display.fill((0, 0, 0))  # Fill the screen with black
        self.draw_map()  # Draw the game map
        self.display.blit(self.weapon.asset, self.weapon.rect)  # Draw the player weapon

        for bullet in self.all_bullets:
            self.display.blit(bullet.bullet_canon, bullet.rect)  # Draw bullets

        for enemy in self.enemies_manager.enemies:
            flipped_image = pg.transform.flip(enemy.image, True, False)  # Flip enemy image horizontally
            self.display.blit(flipped_image, enemy.rect)  # Draw enemies
            enemy.draw_health_bar(self.display)  # Draw health bars for enemies
            self.weapon.health_bar(self.display)  # Draw player health bar
            
        font = pg.font.Font(None, 60)  # Define font for timer
        time_text = font.render(self.timer.get_time(), True, self.white)  # Render timer text
        self.display.blit(time_text, (550, 10))  # Draw timer text on the screen
        
        font = pg.font.Font(None, 50)  # Define font for score
        score_text = font.render(f"Score: {self.score}", True, self.white)  # Render score text
        self.display.blit(score_text, (10, 650))  # Draw score text on the screen

    def game_over(self):
        """Handle game over state."""
        self.handle_enemy_collision()

        if self.end_screen:
            self.img(650, 370, 1300, 750, "menu/background_menu.png")  # Draw background for game over screen
            self.img(630, 140, 320, 110, "menu/logo_game.png")  # Draw game logo
            self.text(60, "GAME OVER", self.dark_red, 480, 300)  # Display game over text
            self.text(43, "PRESS ENTER TO RETURN MENU", self.black, 370, 400)  # Display return to menu prompt
            font = pg.font.Font(None, 43)  # Define font for score display
            score_text = font.render(f"Your score is: {str(self.score)} points", True, self.black)  # Render score text
            self.display.blit(score_text, (425, 500))  # Draw score text on the screen

    def run(self):
        """Main game loop."""
        while self.running:
            super().update()  # Update GUI elements
            self.handle_events()  # Handle user input events
            self.weapon.update()  # Update player weapon
            self.update_shooter()  # Update player and enemy entities
            self.enemies_manager.spawn_enemy()  # Spawn new enemies
            self.draw()  # Draw game elements on the screen

            if self.end_screen:
                self.game_over()  # Handle game over state

            self.timer.update()  # Update game timer
            self.clock.tick(FPS)  # Control frame rate
