import pygame
from pygame.sprite import Sprite
from settings import Settings


class Fighter(Sprite):
    """ describes one enemy fighter """

    def __init__(self, ai_param, screen):
        """initializes fighter and sets it's start position """
        super().__init__()
        self.screen = screen
        self.ai_param = Settings()

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

    def ch_edges(self):
        """returns True if fighter on the edge """
        sc_rect = self.screen.get_rect()
        if self.rect.right >= sc_rect.right or self.rect.left <= 0:
            return True

    def update(self, ai_param):
        """move to the right or left """
        self.x += self.ai_param.f_sp_f * ai_param.f_mv_dir
        self.rect.x = self.x
