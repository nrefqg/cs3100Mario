import pygame
from enemies.enemy0 import Enemy0
from enemies.enemy1 import Enemy1
from enemies.enemy3 import Enemy3
from itertools import combinations

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption("CS 3100 Project")

e1 = Enemy0(300, 500, 3)
e2 = Enemy0(700, 500, -3)
e3 = Enemy1(50, 500, -2)
e4 = Enemy3(900, 500, -2)
enemy_list = pygame.sprite.Group()
enemy_list.add(e1)
enemy_list.add(e2)
enemy_list.add(e3)
enemy_list.add(e4)

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
            first.flip()
            second.flip()
            pygame.display.flip()

    for enemy in enemy_list:
        enemy.move()
        enemy.gravity(SCREEN_HEIGHT)

    if iterations == 250:
        e3.jump(20)
    if iterations == 500:  # test damaging Koopa
        e3.damage(enemy_list)
        e4.damage(enemy_list)
        e1.jump(30)
    if iterations == 1500:  # test that damaging Beetle multiple times does not kill it
        e4.damage(enemy_list)
        e4.damage(enemy_list)

    iterations += 1

    clock.tick(60)
    pygame.display.flip()

pygame.quit()

