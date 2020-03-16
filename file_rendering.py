import pygame
from blocks.blocks import Block
import blocks.pipe
import blocks.redBlock
import file_loader

def render(screen, level):
    block_group = pygame.sprite.Group()
    for x in range(len(level)):
        for y in range(len(level[x])):
            if level[x][y].lower() in 'abcdefghijklmnopqrstuvwxyz':
                #print(level[x][y])
                new_block = Block('redBlock.png', y*16, x*16)
                block_group.add(new_block)
                # screen.blit(pygame.image.load('sprites/redBlock.png'), (y*16, x*16))

    return block_group

def render(screen):
    level = []
    level = file_loader.file_loading()
    levelDisplay = []
    for x in range(len(level)):
        for y in range(len(level[x])):
            if level[x][y].lower() in 'abcdefghijklmnoqrstuvwxyz':
                #print(level[x][y])
                screen.blit(pygame.image.load('sprites/redBlock.png'), (y*16, x*16))
            elif level[x][y].lower() == 'p':
                screen.blit(pygame.image.load('sprites/midPipe.png'), (y*16, x*16))
    return