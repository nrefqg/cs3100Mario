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
from blocks.flagpole import flagpole
from blocks.flagpole import flag


def render(level):
    """
    Translates the level array into groups of usable game objects
    :param level: 2D list of strings that represents the level
    :return: a dictionary of strings that map to sprite groups
        'block' -> block_group
        'pipe' -> pipe_group
    """

    renders = {'ground': None, 'pipe': None, 'breakable': None, 'stone': None, 'hidden': None, 'coin': None, 'power': None, 'flagpole': None, 'flag': None, 'disabled': None}

    block_group = pygame.sprite.Group()
    flag_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    power_group = pygame.sprite.Group()
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
            elif symbol in 'ABCDdefgmnop': #special blocks
                new_block = powerBlock(y*32, x*32)
                power_group.add(new_block)
                renders['power'] = power_group
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
