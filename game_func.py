import sys
import pygame


def check_events():
    """ process buttoms clics and mouse moves """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, ship, bg):
    screen.blit(bg, (0, 0))
    ship.blitme()
    pygame.display.flip()
