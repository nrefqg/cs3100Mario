import pygame
import sys
from pygame.locals import *
import file_loader
import file_rendering


level = []

pygame.init()
#Sets the window title to Super Mario
pygame.display.set_caption('Super Mario')
#Pygame clock that is used to keep game updating at 60 fps
clock = pygame.time.Clock()
# Start writing game code here

display = (500, 500)
scale = pygame.Surface((300, 200))
screen = pygame.display.set_mode(display, 0, 32)


level = file_loader.file_loading()

allRects = file_rendering.render(screen, level)

player_image = pygame.image.load('character/mario.png')

moving_right = False
moving_left = False

player_location = [20,183]
player_rect = pygame.Rect(100, 100, 5, 13)


while True:
    #Fills the background with a light blue color
    screen.fill((146, 244, 255))

    #A list of all rects in the level
    allRects = file_rendering.render(screen, level)
  
    #Movement for the player is modified when specific keypresses are made
    if moving_right == True:
        player_location[0] += 1
        player_location[0] += 1
        player_location[0] += 1
        player_location[0] += 1
        player_location[0] += 1
        player_location[0] += 1
    if moving_left == True:
        player_location[0] -= 1
        player_location[0] -= 1
        player_location[0] -= 1
        player_location[0] -= 1
        player_location[0] -= 1
        player_location[0] -= 1

    #Update player location on the screen
    screen.blit(player_image, player_location)

    #Check pygame for "events" such as button presses
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

    #Update the pygame screen
    scale.blit(pygame.transform.scale(screen, display), (0,0))
    pygame.display.update()
    #Keeps game at 60fps
    clock.tick(60)