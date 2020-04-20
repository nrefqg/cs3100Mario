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
from victory import playerWin

SKY_COLOR = (146, 244, 255)


#VARIABLES HOLDING THE SPRITE LOCATIONS FOR OUR CHARACTER
smallMario = ['sprites/mario.png', 'sprites/marioflip.png']
bigMario = ['character/bigmario.png', 'character/bigmarioflip.png']


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
power_list = renders['power']
pipe_list = renders['pipe']
brick_list = renders['breakable']
coin_list = renders['coin']
hidden_list = renders['hidden']
enemy_list = renders['enemies']
block_list.add(power_list)
block_list.add(brick_list)

if(hidden_list != None):
    block_list.add(hidden_list)

flag_list = renders['flag']
pipe_list = renders['pipe']
flagLoc = []

# Load in image sprite
player = Character(140, 20)


# Initialize viewport
viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)
# Load in main menu screen
viewport.game_menu()

# A list of all rects in the level
allRects = file_rendering.render(level)

#Get the lowest block in the level's y position
for block in block_list:
    if(block.rect.y > lowestTile):
        lowestTile = block.y

#Was trying to get flagpole to work right
for block in allRects['flagpole']:
    if(isinstance(block, flagpole) == True):
        flagLoc.append([block.xHitRight])

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
    # default gravity if mario is in air and not jumping
    if not player.getJumping():
        player.setVertical(False)
        if player.getDeltaY() > 0:
            player.setY_momentum(player.getY_momentum() + .9)
        if player.getDeltaY() + player.getY_momentum() > 0:
            player.setY_location(player.getY_location() + player.getY_momentum())
            player.setDeltaY(player.getDeltaY() + player.getY_momentum())
        else:
            player.setDeltaY(0)
            player.setY_momentum(0)
    else:   # handles mario jump momentum
        if player.getDeltaY() >= 0 and player.getDeltaY() <= 48:
            player.setY_momentum(player.getY_momentum() + 1)
            player.setVertical(True)
        elif player.getDeltaY() > 48 and player.getDeltaY() <= 96:
            player.setY_momentum(player.getY_momentum() + 0.5)
        elif player.getDeltaY() > 96 and player.getDeltaY() <= 140:
            player.setY_momentum(player.getY_momentum() - 1)
            player.setVertical(False)
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
        if(player.powerLevel == 0):
            player.updateImage(smallMario[0])
        elif(player.powerLevel == 1):
            player.updateImage(bigMario[0])
        player.setX_location(player.getX_location() + player.getX_momentum())
    
    if player.getMoveLeft() == True and player.getX_location() > viewport.offsetX:
        if(player.powerLevel == 0):
            player.updateImage(smallMario[1])
        elif(player.powerLevel == 1):
            player.updateImage(bigMario[1])
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
    viewport.render_sprites(player, enemy_list, block_list, pipe_list, flag_list)
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
    #if len(playerGround) > 0:
    #for block in playerGround:
    #player.groundBlockContact(block)
    player.touch(playerGround)
    
    animation += 1
    if animation >= 15:
        block_list.update()
        pygame.display.flip()
        animation = 0

    flagTouch = pygame.sprite.spritecollide(player, renders['flagpole'], False)

    if(flagTouch in renders['flagpole']):
        player, viewport, renders, block_list, pipe_list, enemy_list = playerWin(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH, level)

    #If player is below lowest tile, kill them
    if(player.getY_location() > lowestTile+5):
        player, viewport, renders, block_list, pipe_list, enemy_list = playerDeath(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH, level, level_info)

    level_info.tick()
    pygame.display.update()
    clock.tick(60)  # Keeps game at 60fps
