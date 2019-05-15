import sys
import pygame
from bullet import Bullet


def check_kd_events(event, ai_param, screen, ship, bullets):
    """reacts on the button pushing"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_LSHIFT:
        ship.ai_param.ship_sp_f *= 10
    elif event.key == pygame.K_SPACE:
        fire(ai_param, screen, ship, bullets)


def check_ku_events(event, ship):
    """ reacts on the button leaving """
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False
    elif event.key == pygame.K_LSHIFT:
        ship.ai_param.ship_sp_f /= 10


def check_events(ai_param, screen, ship, bullets):
    """ process buttons clicks and mouse moves """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kd_events(event, ai_param, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_ku_events(event, ship)


def update_screen(ai_param, screen, ship, bg, bullets):
    """updates screen and draws new image on it"""
    screen.blit(bg, (0, 0))
    for bul in bullets.sprites():
        bul.draw_bul()
    ship.blitme()
    pygame.display.flip()


def fire(ai_param, screen, ship, bullets):
    """new bullet creating and adding it to the sprites group"""
    if len(bullets) < ai_param.bul_allowed:
        n_bul = Bullet(ai_param, screen, ship)
        bullets.add(n_bul)


def update_bul(bullets):
    """updates bullets position and remove old one"""
    # updating pos
    bullets.update()
    # removing old
    for bul in bullets.copy():
        if bul.rect.bottom <= 0:
            bullets.remove(bul)
