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

player_image = pygame.image.load('character/mario.png')

moving_right = False
moving_left = False

player_location = [50,50]

while True:

    screen.blit(player_image, player_location)

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Stop pygame
            sys.exit() #Stop script
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()
    #Keeps game at 60fps
    clock.tick(60)