import pygame

class Timer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.time_passed = 0
        self.last_tick = pygame.time.get_ticks()

    def update(self):
        current_tick = pygame.time.get_ticks()
        self.time_passed += current_tick - self.last_tick
        self.last_tick = current_tick

    def get_time(self):
        seconds = self.time_passed // 1000
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"