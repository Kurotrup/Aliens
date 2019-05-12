import pygame
import os
from settings import Settings
from ship import Ship
import game_func as gf


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((ai_param.scn_wth, ai_param.scn_hth))
    pygame.display.set_caption("A l i e n s")
    bg = pygame.image.load(ai_param.bg)
    ship = Ship(ai_param, screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(screen, ship, bg)


ai_param = Settings()
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (ai_param.start_x, ai_param.start_y)


run_game()
# page 234 creating Settings calass
