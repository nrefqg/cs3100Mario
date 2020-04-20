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
    time.sleep(5)

    #RELOAD LEVEL
    # Load in block sprites
    renders = file_rendering.render(level)  # load level from Excel file
    block_list = renders['ground']
    power_list = renders['power']
    pipe_list = renders['pipe']
    brick_list = renders['breakable']
    coin_list = renders['coin']
    hidden_list = renders['hidden']
    single_coin_group = renders['singleCoin']
    star_group = renders['star']
    oneUp_group = renders['oneUp']
    multi_group = renders['multiCoin']
    enemy_list = renders['enemies']
    powerup_list = pygame.sprite.Group()
    
    if(power_list != None):
        block_list.add(power_list)
    
    block_list.add(brick_list)
    block_list.add(pipe_list)
    
    if(single_coin_group != None):
        block_list.add(single_coin_group)
    
    if(star_group != None):
        block_list.add(star_group)
    
    if(oneUp_group != None):
        block_list.add(oneUp_group)
    
    if(multi_group != None):
        block_list.add(multi_group)
    
    if(coin_list != None):
        block_list.add(coin_list)
    
    if(hidden_list != None):
        block_list.add(hidden_list)
    
    flag_list = renders['flag']
    pipe_list = renders['pipe']
    flagLoc = []
    
    # Load in image sprite
    player = Character(140, 20)
    player.powerUp(2)
    viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)

    return player, viewport, renders, block_list, enemy_list