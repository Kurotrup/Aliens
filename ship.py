import pygame
import pyganim


class Ship:
    def __init__(self, ai_param, screen):
        """Initialize ship and sets it start position """
        self.screen = screen
        self.ai_param = ai_param

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
        self.rect.bottom = self.screen_rect.bottom - 10
        self.center = float(self.rect.centerx)
        # moviing flag
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """draws ship in the current position """
        # self.screen.blit(self.image, self.rect)
        self.aob.blit(self.screen, self.rect)

    def update(self):
        """changes ship position according to the move flag state """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_param.ship_sp_f
        elif self.move_left and self.rect.left > 0:
            self.center -= self.ai_param.ship_sp_f
        self.rect.centerx = self.center
