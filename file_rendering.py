import pygame
from blocks.blocks import Block
from blocks.pipe import leftPipe
from blocks.pipe import rightPipe
from blocks.pipe import topPipe
from blocks.pipe import hiddenPipe
from blocks.stone import stone
from blocks.breakableBlock import breakableBlock
from blocks.redBlock import ground
from blocks.hiddenBlock import hiddenBlock
from blocks.coin import coin
from blocks.powerBlock import powerBlock
from blocks.singleCoin import singleCoin
from blocks.multiCoin import multiCoin
from blocks.star import star
from blocks.oneUp import oneUp
from blocks.flagpole import flagpole
from blocks.flagpole import flag
from enemies.enemy0 import Enemy0
from enemies.enemy1 import Enemy1
from enemies.enemy3 import Enemy3


def render(level):
    """
    Translates the level array into groups of usable game objects
    :param level: 2D list of strings that represents the level
    :return: a dictionary of strings that map to sprite groups
        'block' -> block_group
        'pipe' -> pipe_group
    """

    renders = {'ground': None, 'pipe': None, 'breakable': None, 'stone': None, 'hidden': None, 'coin': None, 'power': None, 'flagpole': None, 'flag': None, 
    'disabled': None, 'enemies': None, 'singleCoin': None, 'multiCoin': None, 'star': None, 'oneUp': None}

    block_group = pygame.sprite.Group()
    flag_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    power_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    single_coin_group = pygame.sprite.Group()
    star_group = pygame.sprite.Group()
    oneUp_group = pygame.sprite.Group()
    multi_group = pygame.sprite.Group()

    for x in range(len(level)):
        for y in range(len(level[x])):
            symbol = level[x][y]
            if symbol == 'a': #ground block
                new_block = ground(y*32, x*32) 
                block_group.add(new_block)
                renders['ground'] = block_group
            elif symbol == 'b': #stone block
                new_block = stone(y*32, x*32)
                block_group.add(new_block)
                renders['stone'] = block_group
            elif symbol == 'c': #breakable block
                new_block = breakableBlock(y*32, x*32)
                brick_group.add(new_block)
                renders['breakable'] = brick_group
            elif symbol == 'A': #Single coin block
                new_block = singleCoin(y*32, x*32)
                single_coin_group.add(new_block)
                renders['singleCoin'] = single_coin_group
            elif symbol == 'B' or symbol == 'e' or symbol == 'n':
                new_block = powerBlock(y*32, x*32)
                power_group.add(new_block)
                renders['power'] = power_group
            elif symbol == 'C' or symbol == 'f' or symbol == 'o':
                new_block = star(y*32, x*32)
                star_group.add(new_block)
                renders['star'] = star_group
            elif symbol == 'D' or symbol == 'g' or symbol == 'p':
                new_block = oneUp(y*32, x*32)
                oneUp_group.add(new_block)
                renders['oneUp'] = oneUp_group
            elif symbol == 'd' or symbol == 'm':
                new_block = multiCoin(y*32, x*32)
                multi_group.add(new_block)
                renders['multiCoin'] = multi_group

            elif symbol in 'FGH': #hidden blocks
                new_block = hiddenBlock(y*32, x*32)
                block_group.add(new_block)
                renders['hidden'] = block_group
            elif symbol == 'hq': #dead blocks
                new_block = disabledBlock(y*32, x*32)
                block_group.add(new_block)
                renders['disabled'] = block_group
            elif symbol == 'E': #coins
                new_block = coin(y*32, x*32)
                block_group.add(new_block)
                renders['coin'] = block_group
            elif symbol == 'P': #pipes
                if level[x][y-1] != 'P':
                    new_pipe = leftPipe(y*32, x*32)
                    pipe_group.add(new_pipe)
                else:
                    new_pipe = rightPipe(y*32, x*32)
                    pipe_group.add(new_pipe)
                renders['pipe'] = pipe_group
            elif symbol == 'Q' or symbol == 'R': #usable pipes
                new_pipe = topPipe(y*32, x*32)
                pipe_group.add(new_pipe)
                renders['pipe'] = pipe_group
            elif symbol == '|': #special pipes
                new_pipe = hiddenPipe(y*32, x*32)
                pipe_group.add(new_pipe)
                renders['pipe'] = pipe_group
            elif symbol == '~': #flagpole
                new_block = flagpole(y*32, x*32)
                flag_group.add(new_block)
                renders['flagpole'] = flag_group
            elif symbol == '0' or symbol == '5':
                new_block = Enemy0(y*32, x*32,0)
                enemy_group.add(new_block)
                renders['enemies'] = enemy_group
            elif symbol == '1' or symbol == '6':
                new_block = Enemy1(y*32, x*32, 0)
                enemy_group.add(new_block)
                renders['enemies'] = enemy_group
            elif symbol == '3' or symbol == '8':
                new_block = Enemy3(y*32, x*32, 0)
                enemy_group.add(new_block)
                renders['enemies'] = enemy_group
            if symbol == ' ': #special cases where empty spaces need to change to look better
                if x < len(level)-1 and y < len(level[x])-1:
                    if level[x+1][y] == 'P':
                        new_pipe = topPipe(y*32, x*32)
                        pipe_group.add(new_pipe)
                        renders['pipe'] = pipe_group
                    if level[x][y+1] == '~' and level[x-1][y+1] == ' ':
                        new_block = flag(y*32, x*32)
                        flag_group.add(new_block)
                        renders['flag'] = flag_group

    return renders
