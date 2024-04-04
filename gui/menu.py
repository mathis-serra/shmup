import pygame
from Main_game.Game import Game
from gui.element import Element

class Menu(Element):
    def __init__(self):
        super().__init__()
        self.home_page = True
        self.menu_page = False
        self.cursor_position = 0

    def text_button_menu(self):
        button_labels = ["Jouer", "Option", "Quitter"]
        for idx, label in enumerate(button_labels):
            x = 535
            y = 250 + 100 * idx
            self.text(50, label, self.light_black, x, y)
            if self.cursor_position == idx:
                self.text(55, ">", self.dark_red, 510, y)

    def home(self):
        self.menu_run = True
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_run = False  # Gracefully exit the loop

                elif event.type == pygame.KEYDOWN:
                    if self.home_page:
                        if event.key == pygame.K_RETURN:
                            self.home_page = False
                            self.menu_page = True
                    elif self.menu_page:
                        if event.key == pygame.K_UP:
                            self.cursor_position = (self.cursor_position - 1) % 3
                        elif event.key == pygame.K_DOWN:
                            self.cursor_position = (self.cursor_position + 1) % 3  # Déplacer le curseur vers le bas
                        elif event.key == pygame.K_RETURN and self.cursor_position == 0:
                            game = Game()
                            game.run() 
                        elif event.key == pygame.K_RETURN and self.cursor_position == 1:
                            print("Option")                           
                        elif event.key == pygame.K_RETURN and self.cursor_position == 2:  # Si sur "Quitter"
                            self.menu_run = False

            if self.home_page:
                self.img(650, 370, 1300, 750, "menu/background_home.jpg")
                self.text(42, "Appuyer sur ENTRER pour COMMENCER !", self.white, 520, 640)

            if self.menu_page:
                self.img(350, 350, 1400, 750, "menu/background_menu.png")
                self.img(570, 350, 300, 350, "menu/parchemin_menu.png")
                self.text_button_menu() 

            self.update()

    # def handle_menu_action(self):
    #     if self.cursor_position == 0:
    #         game = Game()
    #         game.run()
    #     elif self.cursor_position == 1:
    #         print("Option")
    #     elif self.cursor_position == 2:
    #         self.menu_run = False  # Gracefully exit the loop
