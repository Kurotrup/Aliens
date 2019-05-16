import pygame
from pygame.sprite import Sprite


class Fighter(Sprite):
    """ describes one enemy fighter """

    def __init__(self, ai_param, screen):
        """initializes fighter and sets it's start position """
        super().__init__()
        self.screen = screen

        # image uploading
        self.image = pygame.image.load("pic/55.png")
        self.rect = self.image.get_rect()

        # every new fighter appears in the left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # position in float
        self.x = float(self.rect.x)

    def blitme(self):
        """ shows fighter in the current position """
        self.screen.blit(self.image, self.rect)
