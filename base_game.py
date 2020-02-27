import pygame
from enemy import Enemy
from hitbox import Hitbox
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("CS 3100 Project")

game_ended = False
clock = pygame.time.Clock()

while not game_ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

