import pygame
import pyganim


class Ship:
    def __init__(self, screen):
        """Initialize ship and sets it start position """
        self.screen = screen

        # image upload in rect
        self.aob = pyganim.PygAnimation(
            [("pic/41.png", 50), ("pic/42.png", 50), ("pic/43.png", 50)]
        )
        self.aob.play()
        self.image = pygame.image.load("pic/41.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # every new ship appears in the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draws ship in the current position """
        # self.screen.blit(self.image, self.rect)
        self.aob.blit(self.screen, self.rect)
