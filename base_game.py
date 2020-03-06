import pygame
from enemy0 import Enemy0
from enemy1 import Enemy1
from pygame.locals import *
from itertools import combinations

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("CS 3100 Project")

e1 = Enemy0(300, 500, 3)
e2 = Enemy0(700, 500, -3)
e3 = Enemy1(50, 500, 2)
enemy_list = pygame.sprite.Group()
enemy_list.add(e1)
enemy_list.add(e2)
enemy_list.add(e3)

game_ended = False
clock = pygame.time.Clock()

iterations = 1

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

    if iterations == 500:  # test damaging Koopa
        e3.damage(enemy_list)
    iterations += 1

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

