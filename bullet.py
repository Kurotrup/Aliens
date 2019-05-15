import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """calss for ruling players bullets"""

    def __init__(self, ai_param, screen, ship):
        """creats bullet object in current ships position """
        super().__init__()
        self.screen = screen

        # bullelt creats in 0,0 position and then moves to the needed position
        self.rect = pygame.Rect(0, 0, ai_param.bul_w, ai_param.bul_h)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # bulet pos in float
        self.y = float(self.rect.y)

        self.color = ai_param.bul_col
        self.sp_f = ai_param.bul_sp_f

    def update(self):
        """moves bulet to the top of the screen"""
        # changing bullet positti on in float
        self.y -= self.sp_f
        # changing rect's pos
        self.rect.y = self.y

    def draw_bul(self):
        """draws bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
