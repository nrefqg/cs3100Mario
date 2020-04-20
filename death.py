#This file contains the code that is used for handling player death

import time
import pygame
import file_rendering
from enemies.enemy0 import Enemy0
from enemies.enemy1 import Enemy1
from enemies.enemy3 import Enemy3
from character import Character
from viewport import Viewport

def playerDeath(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH, level):
    viewport.render_death_message()
    pygame.display.update()
    time.sleep(3)

    #RELOAD LEVEL
    # Load in block sprites
    # Load in block sprites
    renders = file_rendering.render(level)  # load level from Excel file
    block_list = renders['ground']
    power_list = renders['power']
    pipe_list = renders['pipe']
    brick_list = renders['breakable']
    coin_list = renders['coin']
    hidden_list = renders['hidden']
    enemy_list = renders['enemies']
    
    block_list.add(power_list)
    block_list.add(brick_list)
    
    if(hidden_list != None):
        block_list.add(hidden_list)
    
    flag_list = renders['flag']
    pipe_list = renders['pipe']

    # Load in image sprite
    player = Character(140, 20)

    #END RELOAD
    player = Character(140, 20)
    viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)

    return player, viewport, renders, block_list, pipe_list, enemy_list