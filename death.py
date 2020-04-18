#This file contains the code that is used for handling player death

import time
import pygame
from character import Character
from viewport import Viewport

def playerDeath(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH):
    viewport.render_death_message()
    pygame.display.update()
    time.sleep(3)

    player = Character(140, 20)
    viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)

    return player, viewport