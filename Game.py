import pygame as pg 
from gui.element import Element
from gui.menu import Menu


class Game():
    
    def __init__(self):
        self.menu = Menu()
        self.menu.home()