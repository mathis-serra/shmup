import pygame

class Element:
    def __init__(self):
        self.W = 850
        self.H = 750
        self.Screen = pygame.display.set_mode((self.W, self.H))
        pygame.display.set_caption("See of Shump")
        self.clock = pygame.time.Clock()
        self.white = (255,255,255)
        self.brown = (140, 63, 63)
        self.black = (0, 0, 0)
        self.light_black = (56, 53, 53)
        self.grey = (209, 198, 198)
        self.dark_red = (211, 38, 38)
        
    def img(self, x, y, width, height, image_name):
        image = pygame.image.load(f'assets/{image_name}')
        image = pygame.transform.scale(image, (width, height))
        self.Screen.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def img_background(self, x, y, width, height, image_name):
        image = pygame.image.load(f'assets/{image_name}').convert()
        image = pygame.transform.scale(image, (width, height))
        image.set_alpha(115)
        self.Screen.blit(image, (x - image.get_width()//2, y - image.get_height()//2))

    def text(self, text_size, text_content, color, x, y):
        font = pygame.font.Font('gui/font/CampanaScript_PERSONAL_USE_ONLY.otf', text_size)
        text = font.render(text_content, True, color)
        text_rect = text.get_rect(topleft=(x, y))
        self.Screen.blit(text, text_rect)  


    def text_align(self, text_size, text_content,color, x, y):
        font = pygame.font.Font('gui/font/CampanaScript_PERSONAL_USE_ONLY.otf', text_size) 
        text = font.render(text_content, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.Screen.blit(text, text_rect)

    def solid_rect(self,color, x, y, width, height):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x , y, width, height))
    
    def solid_rect_radius(self, color, x, y, width,height , radius):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y,width, height),0,radius)   

    def light_rect(self, color, x, y, width, height, epaisseur):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y, width, height),  epaisseur, 5)

    def light_rect_radius(self, color, x, y, width, height, epaisseur, radius):
        pygame.draw.rect(self.Screen, color, pygame.Rect(x, y, width, height),  epaisseur, radius)
                
    def draw_overlay(self, coloralpha, x, y, width, height):
        overlay_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay_surface.fill(coloralpha)
        self.Screen.blit(overlay_surface, (x, y))
        
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
        
    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.Screen.fill((0, 0, 0))
    
    def update_no_fill(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)

    def get_size(self):
        return self.Screen.get_size()

    def get_display(self):
        return self.Screen
    
    