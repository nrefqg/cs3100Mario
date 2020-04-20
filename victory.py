#This file houses the function the handles a victory state
import time
import pygame
import file_rendering
from enemies.enemy0 import Enemy0
from enemies.enemy1 import Enemy1
from enemies.enemy3 import Enemy3
from character import Character
from viewport import Viewport

def playerWin(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH, level):
    viewport.render_victory_message()
    pygame.display.update()
    time.sleep(3)

    #RELOAD LEVEL
    # Load in block sprites
    renders = file_rendering.render(level)  # load level from Excel file
    block_list = renders['ground']
    pipe_list = renders['pipe']
    flagLoc = []

    # Load in image sprite
    player = Character(140, 20)

    # Load in enemy list
    enemy_list = pygame.sprite.Group()
    e0 = Enemy0(400, 20, -1)
    e1 = Enemy1(100, 20, 2)
    e3 = Enemy3(200, 20, 1)
    for e in [e0, e1, e3]:
        enemy_list.add(e)

    #END RELOAD
    player = Character(140, 20)
    viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)

    return player, viewport, renders, block_list, pipe_list, enemy_list