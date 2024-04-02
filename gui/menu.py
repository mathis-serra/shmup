from gui.element import Element
import pygame
class Menu(Element):
    def __init__(self):
        Element.__init__(self)
        self.home_page = True
        self.menu_page = False
    
    def home(self):
        self.menu_run = True
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                                    
                # Event keyboard
                elif event.type == pygame.KEYDOWN:
                    pass
            
            self.update()
        