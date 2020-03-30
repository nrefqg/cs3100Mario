import pygame
from blocks.blocks import Block
from blocks.pipe import midPipe


def render(level):
    """
    Translates the level array into groups of usable game objects
    :param level: 2D list of strings that represents the level
    :return: a dictionary of strings that map to sprite groups
        'block' -> block_group
        'pipe' -> pipe_group
    """

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
