import pygame
import os
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_func as gf


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((ai_param.scn_wth, ai_param.scn_hth))
    pygame.display.set_caption("A l i e n s")
    bg = pygame.image.load(ai_param.bg)
    ship = Ship(ai_param, screen)
    bullets = Group()
    fighters = Group()
    gf.imperials(ai_param, screen, ship, fighters)
    while True:
        gf.check_events(ai_param, screen, ship, bullets)
        ship.update()
        gf.update_bul(bullets)
        gf.update_screen(ai_param, screen, ship, bg, fighters, bullets)


ai_param = Settings()
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (ai_param.start_x, ai_param.start_y)


run_game()
# page 234 creating Settings calass
