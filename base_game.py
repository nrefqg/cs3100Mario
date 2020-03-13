import pygame
import sys
from pygame.locals import *
import file_rendering
import file_loader
from enemies.enemy0 import Enemy0

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

enemy_list = pygame.sprite.Group()
e0 = Enemy0(100, 20, 2)
enemy_list.add(e0)

iterations = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Stop pygame
            sys.exit() #Stop script

    screen.fill((146, 244, 255))
    block_list = file_rendering.render(screen, level)
    block_list.draw(screen)
    enemy_list.draw(screen)
    e0.move()
    e0.gravity(500)

    collisions = pygame.sprite.groupcollide(enemy_list, block_list, False, False)
    enemy_collisions = set(collisions.keys())
    for e in enemy_collisions:
        if e.yspeed > 0:
            e.yspeed = 0

    iterations += 1
    if iterations == 100:
        print("jump!")
        e0.jump(20)

    pygame.display.update()
    #Keeps game at 60fps
    clock.tick(60)
