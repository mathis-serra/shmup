from gui.element import Element
import pygame

class Menu(Element):
    def __init__(self):
        super().__init__()
        self.home_page = True
        self.menu_page = False
        
    def button_menu(self):
        self.text(55,"Jouer",self.dark_red,535,70)
        self.text(50,"Option",self.dark_red,525,170)
        self.text(50,"Quitter",self.dark_red,525,270)
        

    def home(self):
        self.menu_run = True
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Event keyboard
                elif event.type == pygame.KEYDOWN and self.home_page:
                    self.home_page = False
                    self.menu_page = True

            if self.home_page:
                self.img(350, 350, 1400, 750, "menu/background_home.jpg")
                self.text(40, "Appuyer sur ENTRER pour COMMENCER !", self.white, 250, 640)

            if self.menu_page:
                self.img(350, 350, 1400, 750, "menu/background_menu.png")
                self.button_menu()
                

            self.update()
