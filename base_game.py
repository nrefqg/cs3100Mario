import pygame
import sys
import file_rendering
import file_loader
from enemies.enemy0 import Enemy0

pygame.init()
pygame.display.set_caption('Super Mario')  # Sets the window title
clock = pygame.time.Clock()  # Pygame clock that is used to keep game updating at 60 fps

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

display = (SCREEN_WIDTH, SCREEN_HEIGHT)
scale = pygame.Surface((300, 200))
screen = pygame.display.set_mode(display, 0, 32)  # set the screen dimensions
level = file_loader.file_loading()
block_list = file_rendering.render(screen, level)  # load level from Excel file

enemy_list = pygame.sprite.Group()
e0 = Enemy0(400, 20, -2)
enemy_list.add(e0)

iterations = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Stop pygame
            sys.exit()  # Stop script

    screen.fill((146, 244, 255))
    block_list.draw(screen)
    enemy_list.draw(screen)
    e0.move()
    e0.gravity(500)

    collisions = pygame.sprite.groupcollide(enemy_list, block_list, False, False)
    for enemy, blocks in collisions.items():
        if len(blocks) > 0:
            primary_block = blocks[0]
            enemy.gravity(primary_block.rect.y)

    iterations += 1
    if iterations % 100 == 0:
        e0.jump(20)

    pygame.display.update()
    clock.tick(60)  # Keeps game at 60fps
