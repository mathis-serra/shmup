import pygame
import sys

class Timer:
    def __init__(self):
        self.time_passed = 0
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)  # Timer événement toutes les secondes

    def update(self):
        self.time_passed += 1

    def get_time(self):
        hours = self.time_passed // 3600
        minutes = (self.time_passed % 3600) // 60
        seconds = self.time_passed % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pirates")
        self.clock = pygame.time.Clock()
        self.timer = Timer()

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == self.timer.timer_event:
                    self.timer.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)

    def draw(self):
        font = pygame.font.Font(None, 36)
        time_text = font.render(f"{self.timer.get_time()}", True, (255, 255, 255))
        text_rect = time_text.get_rect()
        text_rect.topright = (780, 20)  # Position en haut à droite
        self.screen.blit(time_text, text_rect)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
