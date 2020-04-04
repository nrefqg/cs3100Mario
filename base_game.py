import pygame
import sys
import file_rendering
import file_loader
from itertools import combinations
from enemies.enemy0 import Enemy0
from enemies.enemy1 import Enemy1
from enemies.enemy3 import Enemy3

pygame.init()
pygame.display.set_caption('Super Mario')  # Sets the window title
clock = pygame.time.Clock()  # Pygame clock that is used to keep game updating at 60 fps

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
animation = 0
display = (SCREEN_WIDTH, SCREEN_HEIGHT)
scale = pygame.Surface((300, 200))
screen = pygame.display.set_mode(display, 0, 32)  # set the screen dimensions
level = file_loader.file_loading()

renders = file_rendering.render(level)  # load level from Excel file
block_list = renders['ground']
pipe_list = renders['pipe']

enemy_list = pygame.sprite.Group()
e0 = Enemy0(400, 20, -1)
e1 = Enemy1(100, 20, 2)
e3 = Enemy3(200, 20, 1)
for e in [e0, e1, e3]:
    enemy_list.add(e)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Stop pygame
            sys.exit()  # Stop script

    screen.fill((146, 244, 255))
    block_list.draw(screen)
    if pipe_list is not None:
        pipe_list.draw(screen)
    enemy_list.draw(screen)

    # detect collisions between enemies
    for first, second in combinations(enemy_list, 2):
        if first.rect.colliderect(second.rect):
            first.flip()
            second.flip()
            pygame.display.flip()

    # move all enemies and apply gravity
    for enemy in enemy_list:
        enemy.move()
        enemy.gravity(SCREEN_HEIGHT)

    # detect collisions between enemies and blocks
    collisions = pygame.sprite.groupcollide(enemy_list, block_list, False, False)
    for enemy, blocks in collisions.items():
        if len(blocks) > 0:
            primary_block = blocks[0]
            enemy.gravity(primary_block.rect.y)
    
    animation += 1
    if animation >= 15:
        block_list.update()
        block_list.draw(screen)
        pygame.display.flip()
        animation = 0

    pygame.display.update()
    clock.tick(60)  # Keeps game at 60fps
