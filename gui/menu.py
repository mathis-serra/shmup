from gui.element import Element
import pygame

class Menu(Element):
    def __init__(self):
        super().__init__()
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
                elif event.type == pygame.KEYDOWN and self.home_page:
                    pygame.quit()

            if self.home_page:
                self.img(350, 350, 1400, 750, "menu/background_home1.jpg")

            if self.menu_page:
                pass

            self.update()
