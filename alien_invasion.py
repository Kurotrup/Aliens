import sys
import pygame
import os
from settings import Settings


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((ai_param.scn_wth, ai_param.scn_hth))
    pygame.display.set_caption("A l i e n s")
    bg = pygame.image.load(ai_param.bg)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # screen.fill(bg_color)
        screen.blit(bg, (0, 0))
        pygame.display.flip()


ai_param = Settings()
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (ai_param.start_x, ai_param.start_y)


run_game()
# page 234 creating Settings calass
