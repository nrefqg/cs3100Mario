import pygame
from blocks.blocks import Block
from blocks.pipe import midPipe


def render(level):

    renders = {'block': None, 'pipe': None}

    block_group = pygame.sprite.Group()
    pipe_group = pygame.sprite.Group()
    for x in range(len(level)):
        for y in range(len(level[x])):
            symbol = level[x][y]
            if symbol in 'abcdefghijklmnopqrstuvwxyz':
                new_block = Block('redBlock.png', y*16, x*16)
                block_group.add(new_block)
                renders['block'] = block_group
            elif symbol == 'P':
                new_pipe = midPipe(y*16, x*16)
                pipe_group.add(new_pipe)
                renders['pipe'] = pipe_group

    return renders
