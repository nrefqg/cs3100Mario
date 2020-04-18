import pygame
import sys
import file_rendering
import time
import file_loader
from death import playerDeath
from blocks.flagpole import flagpole
from character import Character
from itertools import combinations
from level import Level
from enemies.enemy0 import Enemy0
from enemies.enemy1 import Enemy1
from enemies.enemy3 import Enemy3
from viewport import Viewport

SKY_COLOR = (7, 155, 176)

level = []

pygame.init()
pygame.display.set_caption('Super Mario')  # Sets the window title
clock = pygame.time.Clock()  # Pygame clock that is used to keep game updating at 60 fps

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
animation = 0
display = (SCREEN_WIDTH, SCREEN_HEIGHT)
scale = pygame.Surface((300, 200))
level = file_loader.file_loading()
level_info = Level([], 400) # Load in level with no sprites and 400 time
lowestTile = 0

# Load in block sprites
renders = file_rendering.render(level)  # load level from Excel file
block_list = renders['ground']
pipe_list = renders['pipe']
flagLoc = []

# Load in image sprite
player = Character(140, 20)

# Load in enemy list
enemy_list = pygame.sprite.Group()
e0 = Enemy0(400, 20, -1)
e1 = Enemy1(100, 20, 2)
e3 = Enemy3(200, 20, 1)
for e in [e0, e1, e3]:
    enemy_list.add(e)

# Initialize viewport
viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)

# A list of all rects in the level
allRects = file_rendering.render(level)

#Get the lowest block in the level's y position
for block in block_list:
    if(block.rect.y > lowestTile):
        lowestTile = block.y

#This while loops contains the running game
while True:
    # Fills the background with a light blue color
    viewport.reset(SKY_COLOR)

    # Sprinting and horizontal movement
    if player.getMoveRight() and player.getX_momentum() < 5.0:
        player.setX_momentum(player.getX_momentum() + 0.25)
    if player.getMoveLeft() and player.getX_momentum() < 5.0:
        player.setX_momentum(player.getX_momentum() + 0.25)
    elif player.getX_momentum() >= 0.1:
        player.setX_momentum(player.getX_momentum() - 0.1)
    else:
        player.setX_momentum(0)
    #"""
    # default gravity if mario is in air and not jumping
    if not player.getJumping():
        if player.getDeltaY() > 0:
            player.setY_momentum(player.getY_momentum() + .3)
        else:
            player.setY_momentum(0)
            player.setDeltaY(0)
        if player.getDeltaY() + player.getY_momentum() > 0:
            temp = player.getY_location()
            player.setY_location(player.getY_location() + player.getY_momentum())
            player.setDeltaY(player.getDeltaY() + player.getY_momentum())
        else:
            player.setDeltaY(0)
            player.setY_momentum(0)
    else:   # handles mario jump momentum
        if player.getDeltaY() >= 0 and player.getDeltaY() <= 48:
            player.setY_momentum(player.getY_momentum() + 1)
        elif player.getDeltaY() > 48 and player.getDeltaY() <= 96:
            player.setY_momentum(player.getY_momentum() + 0.5)
        elif player.getDeltaY() > 96 and player.getDeltaY() <= 140:
            player.setY_momentum(player.getY_momentum() - 1)
        elif player.getDeltaY() > 140:
            player.setY_momentum(player.getY_momentum() - 0.25)

        # handles positioning
        if player.getDeltaY() < 140:
            player.setY_location(player.getY_location() - player.getY_momentum())
            player.setDeltaY(player.getDeltaY() + player.getY_momentum())
        elif player.getDeltaY() >= 61 and player.getDeltaY() < 68:
            player.setY_location(player.getY_location() - 0.1)
            player.setDeltaY(player.getDeltaY() - 0.1)
        else:
            player.setY_momentum(0)
            player.setJumping(False)

    # Movement for the player is modified when specific keypresses are made
    if player.getMoveRight() == True:
        player.updateImage('sprites/mario.png')
        player.setX_location(player.getX_location() + player.getX_momentum())

    if player.getMoveLeft() == True and player.getX_location() > viewport.offsetX:
        player.updateImage('sprites/marioflip.png')
        player.setX_location(player.getX_location() - player.getX_momentum())

    # Check pygame for "events" such as button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()  # Stop pygame
            sys.exit()  # Stop script

        # Respond to player keys
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                player.setMoveRight(True)
            if event.key == pygame.K_LEFT:
                player.setMoveLeft(True)
            if event.key == pygame.K_SPACE and player.getDeltaY() == 0:
                player.setJumping(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.setMoveRight(False)
            if event.key == pygame.K_LEFT:
                player.setMoveLeft(False)
            if event.key == pygame.K_SPACE:
                player.setJumping(False)

    # Update sprites on screen
    viewport.render_sprites(player, enemy_list, block_list, pipe_list)
    # Update level information
    viewport.render_ui(level_info)

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
    enemyGround = pygame.sprite.groupcollide(enemy_list, block_list, False, False)
    for enemy, blocks in enemyGround.items():
        if len(blocks) > 0:
            primary_block = blocks[0]
            enemy.gravity(primary_block.rect.y)

    # checks for standing on a block and continues gravity if not
    playerGround = pygame.sprite.spritecollide(player, block_list, False)
    player.groundContact(playerGround)

    animation += 1
    if animation >= 15:
        block_list.update()
        pygame.display.flip()
        animation = 0

    
    #If player is below lowest tile, kill them
    if(player.getY_location() > lowestTile+5):
        player, viewport, renders, block_list, pipe_list, enemy_list = playerDeath(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH, level)

    level_info.tick()
    pygame.display.update()
    clock.tick(60)  # Keeps game at 60fps
