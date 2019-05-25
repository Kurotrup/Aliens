# Aliens
Alien invasions game from python crash course book

#Project structure
#Folders:
- "pic":
 contains images used in the game

#Files:
- "alien_invasion.py":
  main file of the project which contains such object as:
  - ai_param, game settings
  - screen, main surface
  - ship , player's ship
  - bullets , sprites group of player's bullets
  also it stores main while loop which continuously calling methods:
  - check_events(), process buttons clicks and mouse moves
  - ship.update(), changes ship position
  - update_screen(), updates screen and draws new images on it
  - update_bul(), updates bullets position and remove old one
  For starting the game you need to run only this file, all others files stores the code which is imported in this file.   

- "settings.py":
  this file contains class "Settings" with one method __init__ which initializes game options that rules appearance and game speed

- "game_func.py":
  contains bunch of the main game functions:
  - check_events(), process buttons clicks and mouse moves
  - check_kd_events(), reacts on the button pushing
  - check_ku_events(), reacts on the button leaving
  - update_screen(), updates screen and draws new image on it
  - update_bul(), updates bullets position and remove old one
  - fire(), new bullet creating and adding it to the sprites group
  - imperials(), creates imperials fleet
  - get_numb(), calculating number of fighters in a row
  - cr_fgr(), creates fighter

- "ship.py":
  stores "Ship" class which describes players ship. This class have 3 methods:
  - __init__, initializes object of the class  
  - update(), changes ship position according to the move flag state
  - blitme(), draws ship in the current position  

- "bullet.py":
  stores "Bullet" class which control player's bullets with such methods:
  - __init__(), creates bullet object in current ships position
  - update(), moves bullet to the top of the screen
  - draw_bul(), draws bullet on the screen

- "enemy.py":
  stores "Fighter" class describes one enemy fighter. This class such methods:
  - __init__(), initializes fighter and sets it's start position
  - blitme(), shows fighter in the current position
