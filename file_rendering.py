import pygame
import blocks.blocks
import blocks.pipe
import blocks.redBlock
#import file_loader

def render(screen, level):
    #level = []
    #level = file_loader.file_loading()
    levelDisplay = []
    allRects = []

    for x in range(len(level)):
        for y in range(len(level[x])):
            if level[x][y].lower() in 'abcdefghijklmnoqrstuvwxyz':
                #print(level[x][y])
                screen.blit(pygame.image.load('sprites/redBlock.png'), (y*16, x*16))
            elif level[x][y].lower() == 'p':
                screen.blit(pygame.image.load('sprites/midPipe.png'), (y*16, x*16))
            if(level[x][y] != ' '):
                allRects.append(pygame.Rect(y*16, x*16, 16, 16))

    return allRects