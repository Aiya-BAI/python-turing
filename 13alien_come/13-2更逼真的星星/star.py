import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height



