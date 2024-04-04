from gui.element import Element
import pygame

class Menu(Element):
    def __init__(self):
        super().__init__()
        self.home_page = True
        self.menu_page = False
        self.cursor_position = 0

    def text_button_menu(self):
        self.text(55, "Jouer", self.light_black, 535, 250)
        self.text(50, "Option", self.light_black, 525, 350)
        self.text(50, "Quitter", self.light_black, 525, 450)
        # Draw cursor
        if self.cursor_position == 0:
            self.text(55, ">", self.dark_red, 510, 250)
        elif self.cursor_position == 1:
            self.text(55, ">", self.dark_red, 500, 350)
        elif self.cursor_position == 2:
            self.text(55, ">", self.dark_red, 510, 450)

    def home(self):
        self.menu_run = True
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Gestion des touches du clavier
                elif event.type == pygame.KEYDOWN:
                    if self.home_page:
                        if event.key == pygame.K_RETURN:
                            self.home_page = False
                            self.menu_page = True
                    elif self.menu_page:
                        if event.key == pygame.K_UP:
                            self.cursor_position = (self.cursor_position - 1) % 3  # Déplacer le curseur vers le haut
                        elif event.key == pygame.K_DOWN:
                            self.cursor_position = (self.cursor_position + 1) % 3  # Déplacer le curseur vers le bas
                        elif event.key == pygame.K_RETURN and self.cursor_position == 2:  # Si sur "Quitter"
                            pygame.quit()

            if self.home_page:
                self.img(350, 350, 1400, 750, "menu/background_home.jpg")
                self.text(40, "Appuyer sur ENTRER pour COMMENCER !", self.white, 250, 640)

            if self.menu_page:
                self.img(350, 350, 1400, 750, "menu/background_menu.png")
                self.img(570, 350, 300, 350, "menu/parchemin_menu.png")
                self.text_button_menu() 

            self.update()
