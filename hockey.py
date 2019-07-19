# Librerias e importaciones
import sys, pygame
from pygame.locals import *

# medidas de la ventana
WIDTH = 1165
HEIGHT = 800
# creacion del proyecto por clases
#clase de puck
class Puck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("/*imagen*/", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.4, -0.4]