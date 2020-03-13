import pygame
import sys
from pygame.locals import *
import file_rendering

pygame.init()
#Sets the window title to Super Mario
pygame.display.set_caption('Super Mario')
#Pygame clock that is used to keep game updating at 60 fps
clock = pygame.time.Clock()
# Start writing game code here

display = (500, 500)
scale = pygame.Surface((300, 200))
screen = pygame.display.set_mode(display, 0, 32)
screen.fill((146, 244, 255))

file_rendering.render(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Stop pygame
            sys.exit() #Stop script

    pygame.display.update()
    #Keeps game at 60fps
    clock.tick(60)
