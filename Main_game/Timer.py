import pygame

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