import pygame
from enemy import Enemy
from enemy1 import Enemy1
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("CS 3100 Project")

enemy1 = Enemy1(300, 500)
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy1)

game_ended = False
clock = pygame.time.Clock()

while not game_ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True

    screen.fill((100, 177, 232))

    enemy_list.draw(screen)
    for enemy in enemy_list:
        enemy.move(4)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

