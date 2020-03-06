import pygame
from enemy import Enemy
from enemy1 import Enemy1
from pygame.locals import *
from itertools import combinations

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("CS 3100 Project")

enemy1 = Enemy1(300, 500, 3)
enemy2 = Enemy1(700, 500, -3)
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy1)
enemy_list.add(enemy2)

game_ended = False
clock = pygame.time.Clock()

while not game_ended:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True

    screen.fill((100, 177, 232))

    enemy_list.draw(screen)

    for first, second in combinations(enemy_list, 2):
        if first.rect.colliderect(second.rect):
            first.speed *= -1
            second.speed *= -1

    for enemy in enemy_list:
        enemy.move()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

