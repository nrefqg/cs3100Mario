import pygame
import sys
import file_rendering
import time
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

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
animation = 0
display = (SCREEN_WIDTH, SCREEN_HEIGHT)
scale = pygame.Surface((300, 200))
#screen = pygame.display.set_mode(display, 0, 32)  # set the screen dimensions
level = file_loader.file_loading()

# Load in block sprites
renders = file_rendering.render(level)  # load level from Excel file
block_list = renders['ground']
pipe_list = renders['pipe']

# Load in image sprite
player_image = pygame.image.load('sprites/mario.png')
player_location = [20,140]
player_rect = pygame.Rect(100, 100, 5, 13)

#default movement indicators
moving_right = False
moving_left = False
jumping = False

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

#initial momentum value
player_x_momentum = 0
player_y_momentum = 0

while True:
    #Fills the background with a light blue color
    viewport.reset()

    #if character falls below floor, resets to floor.  Will fix once collisions are implemented
    if player_location[1] > 208:
        player_location[1] = 208

    #Sprinting and horizontal movement
    if moving_right and player_x_momentum < 5.0:
        player_x_momentum += 0.25
    if moving_left and player_x_momentum < 5.0:
        player_x_momentum += 0.25
    elif player_x_momentum >= 0.1:
        player_x_momentum -= 0.1
    else:
        player_x_momentum = 0

    #default gravity if mario is in air and not jumping
    if not jumping:
        if player_location[1] < 208:
            player_y_momentum += 0.3
        else:
            player_y_momentum = 0

        if player_location[1] + player_y_momentum < 208:
            player_location[1] += player_y_momentum
        else:
            player_location[1] = 208
    else:   #handles mario jump momentum
        if player_location[1] <= 208 and player_location[1] >= 191:
            player_y_momentum += 1
        elif player_location[1] < 191 and player_location[1] >= 174:
            player_y_momentum += 0.5
        elif player_location[1] < 174 and player_location[1] >= 157:
            player_y_momentum -= 1
        elif player_location[1] < 157 and player_location[1] >= 140:
            player_y_momentum -= 0.25

        #handles positioning
        if player_location[1] > 140:
            player_location[1] -= player_y_momentum
        elif player_location[1] <= 147 and player_location[1] > 140:
            player_location[1] -= 0.1
        else:
            player_location[1] = 140
            player_y_momentum = 0
            jumping = False

    #Movement for the player is modified when specific keypresses are made
    if moving_right == True:
        player_image = pygame.image.load('sprites/mario.png')
        player_location[0] += player_x_momentum

    if moving_left == True and player_location[0] > viewport.offsetX:
        player_image = pygame.image.load('sprites/marioflip.png')
        player_location[0] -= player_x_momentum

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
            if event.key == pygame.K_SPACE and player_location[1] == 208:
                jumping = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_SPACE:
                jumping = False
                player_y_momentum = 0

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

    animation += 1
    if animation >= 15:
        block_list.update()
        pygame.display.flip()
        animation = 0

    pygame.display.update()
    clock.tick(60)  # Keeps game at 60fps
