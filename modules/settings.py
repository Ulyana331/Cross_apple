import pygame
import os

pygame.init()

list_settings_window = [420, 420]

def finding_path(name_file):
    path_file = os.path.abspath(__file__ + '/..').split('\\')
    del path_file[-1]
    path_file = os.path.join('\\'.join(path_file), name_file)
    return path_file

class Settings:
    def __init__(self, 
        x= None, 
        y= None, 
        width= None, 
        height= None, 
        color= None, 
        name= None
    ):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        self.NAME = name
        self.IMAGE = None
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        if self.NAME:
            self.load_image()
    
    def load_image(self):
        path_img = finding_path(self.NAME)
        self.IMAGE = pygame.image.load(path_img)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
    
    def blit_sprite(self, window):
        window.blit(self.IMAGE, (self.X, self.Y))