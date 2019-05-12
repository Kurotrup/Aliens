import sys
import pygame


def check_kd_events(event, ship):
    """reacted on the button pushing"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_LSHIFT:
        ship.ai_param.ship_sp_f *= 10


def check_ku_events(event, ship):
    """ reacted on the button releaving """
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_LSHIFT:
        ship.ai_param.ship_sp_f /= 10


def check_events(ship):
    """ process buttoms clics and mouse moves """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kd_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_ku_events(event, ship)


def update_screen(screen, ship, bg):
    """udate scree and draws new image on it """
    screen.blit(bg, (0, 0))
    ship.blitme()
    pygame.display.flip()
