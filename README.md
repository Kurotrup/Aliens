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
  also it stores main while loop which continuously calling methods:
  - check_events(), process buttons clicks and mouse moves
  - ship.update(), changes ship position according
  - update_screen(), updates screen and draws new image on it
  For starting the game you need to run only this file, all others files stores the code which is imported in this file.   

- "settings.py":
  this file contains class "Settings" with one method __init__ which initializes game options that rules appearance and game speed

- "game_func.py":
  contains bunch of the main game functions:
  - check_events(), process buttons clicks and mouse moves
  - check_kd_events(), reacts on the button pushing
  - check_ku_events(), reacts on the button leaving
  - update_screen(), updates screen and draws new image on it

- "ship.py":
  stores "Ship" class which describes players ship. This class have 3 methods:
  - __init__, initializes object of the classS  
  - update(), changes ship position according to the move flag state
  - blitme(), draws ship in the current position  

- "bullet.py"
