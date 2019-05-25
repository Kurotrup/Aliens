import sys
import pygame
from bullet import Bullet
from enemy import Fighter


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_param, screen, ship, bg, fighters, bullets):
    """updates screen and draws new image on it"""
    screen.blit(bg, (0, 0))
    for bul in bullets.sprites():
        bul.draw_bul()
    ship.blitme()
    fighters.draw(screen)
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


def imperials(ai_param, screen, ship, fighters):
    """creates imperials fleet """
    # fighter's creation and calculating the amount of fighters
    fighter = Fighter(ai_param, screen)
    fi_amount_x = get_numb(ai_param, fighter.rect.width)
    row_n = row_numb(ai_param, ship.rect.height, fighter.rect.height)
<<<<<<< HEAD
    # rows creation
=======
    # fist row creation
    print(row_n)
>>>>>>> 04a3dea872796abdaa4a00f9de94e8add12dc9b4
    for r in range(row_n):
        for fi in range(fi_amount_x):
            cr_fgr(ai_param, screen, fighters, fi, r)


def get_numb(ai_param, fighter_w):
    """ calculating number of fighters in a row"""
    av_space_x = ai_param.scn_wth - 2 * fighter_w
    fi_amount = int(av_space_x / (2 * fighter_w))
    return fi_amount


def row_numb(ai_param, ship_h, fighter_h):
    """ calculating the number of fighters rows """
    av_space_y = ai_param.scn_hth - (2 * fighter_h) - ship_h
    num_rows = int(av_space_y / (2 * fighter_h))
    return num_rows


def cr_fgr(ai_param, screen, fighters, fi, row_n):
    """creates fighter """
    fighter = Fighter(ai_param, screen)
    fighter_w = fighter.rect.width
    fighter_h = fighter.rect.height
    fighter.x = fighter_w + 2 * fighter_w * fi
    fighter.rect.x = fighter.x
    fighter.rect.y = fighter_h + fighter_w * row_n
    fighters.add(fighter)
