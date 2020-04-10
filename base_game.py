import pygame
import sys
import file_rendering
import file_loader
from itertools import combinations
from enemies.enemy0 import Enemy0
from enemies.enemy1 import Enemy1
from enemies.enemy3 import Enemy3
from viewport import Viewport

level = []

pygame.init()
pygame.display.set_caption('Super Mario')  # Sets the window title
clock = pygame.time.Clock()  # Pygame clock that is used to keep game updating at 60 fps

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

display = (SCREEN_WIDTH, SCREEN_HEIGHT)
scale = pygame.Surface((300, 200))
#screen = pygame.display.set_mode(display, 0, 32)  # set the screen dimensions
level = file_loader.file_loading()

# Load in block sprites
renders = file_rendering.render(level)  # load level from Excel file
block_list = renders['block']
pipe_list = renders['pipe']

# Load in image sprite
player_image = pygame.image.load('character/mario.png')
player_location = [20,208]
player_rect = pygame.Rect(100, 100, 5, 13)

moving_right = False
moving_left = False

# Load in enemy list
enemy_list = pygame.sprite.Group()
e0 = Enemy0(400, 20, -1)
e1 = Enemy1(100, 20, 2)
e3 = Enemy3(200, 20, 1)
for e in [e0, e1, e3]:
    enemy_list.add(e)

# Initialize viewport
viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)

#A list of all rects in the level
allRects = file_rendering.render(level)

while True:
    #Fills the background with a light blue color
    viewport.reset()

    #A list of all rects in the level
    #allRects = file_rendering.render(level)
  
    #Movement for the player is modified when specific keypresses are made
    if moving_right == True:
        player_location[0] += 1
    if moving_left == True:
        player_location[0] -= 1

    #Check pygame for "events" such as button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()  # Stop pygame
            sys.exit()  # Stop script

        # Respond to player keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

    # Update sprites on screen
    viewport.render_sprites(player_image, player_location, enemy_list, block_list, pipe_list)

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

    pygame.display.update()
    clock.tick(60)  # Keeps game at 60fps
