import pygame
import blocks.blocks
import blocks.pipe
import blocks.redBlock
import file_loader

def render(screen):
    level = []
    level = file_loader.file_loading()
    levelDisplay = []
    for x in range(len(level)):
        for y in range(len(level[x])):
            if level[x][y].lower() in 'abcdefghijklmnopqrstuvwxyz':
                #print(level[x][y])
                screen.blit(pygame.image.load('sprites/redBlock.png'), (y*16, x*16))

    return