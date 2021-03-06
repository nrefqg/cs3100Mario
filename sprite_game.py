import pygame
import sys
import file_rendering
import time
import file_loader
from death import playerDeath
from blocks.flagpole import flagpole
from blocks.mushroom import mushroom
from character import Character
from itertools import combinations
from level import Level
from sound import SoundClass
from viewport import Viewport
from victory import playerWin
from enemies.enemy4 import Enemy4

SKY_COLOR = (146, 244, 255)


#VARIABLES HOLDING THE SPRITE LOCATIONS FOR OUR CHARACTER
smallMario = ['sprites/mariosmall.png', 'sprites/marioflipsmall.png']
bigMario = ['sprites/mariobig.png', 'sprites/marioflipbig.png']


level = []

pygame.init()
pygame.display.set_caption('Osmosis Jones')  # Sets the window title
clock = pygame.time.Clock()  # Pygame clock that is used to keep game updating at 60 fps

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
animation = 0
display = (SCREEN_WIDTH, SCREEN_HEIGHT)
scale = pygame.Surface((300, 200))
level = file_loader.file_loading()
level_info = Level([], 14000) # Load in level with no sprites and 400 time
lowestTile = 0

# Load in block sprites
renders = file_rendering.render(level)  # load level from Excel file
block_list = renders['ground']
power_list = renders['power']
pipe_list = renders['pipe']
brick_list = renders['breakable']
coin_list = renders['coin']
hidden_list = renders['hidden']
single_coin_group = renders['singleCoin']
star_group = renders['star']
oneUp_group = renders['oneUp']
multi_group = renders['multiCoin']
enemy_list = renders['enemies']
powerup_list = pygame.sprite.Group()

if(power_list != None):
    block_list.add(power_list)

block_list.add(brick_list)
block_list.add(pipe_list)
projectile_list = pygame.sprite.Group()

if(single_coin_group != None):
    block_list.add(single_coin_group)

if(star_group != None):
    block_list.add(star_group)

if(oneUp_group != None):
    block_list.add(oneUp_group)

if(multi_group != None):
    block_list.add(multi_group)

if(coin_list != None):
    block_list.add(coin_list)

if(hidden_list != None):
    block_list.add(hidden_list)

flag_list = renders['flag']
flagLoc = []

# Load in image sprite
player = Character(140, 20)


# Initialize viewport
viewport = Viewport(SCREEN_WIDTH, SCREEN_HEIGHT)
# Load in main menu screen
viewport.game_menu()
# Initialize Sound
sound_obj = SoundClass()

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

sound_obj.start_bg()

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
        elif player.getDeltaY() > 96 and player.getDeltaY() <= 160:
            player.setY_momentum(player.getY_momentum() - 1)
            player.setVertical(False)
        elif player.getDeltaY() > 160:
             player.setY_momentum(player.getY_momentum() - 0.25)

        # handles positioning
        if player.getDeltaY() < 160:
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
        if(player.powerLevel == 1):
            player.updateImage(smallMario[0])
        elif(player.powerLevel == 2):
            player.updateImage(bigMario[0])
        player.setX_location(player.getX_location() + player.getX_momentum())
    
    if player.getMoveLeft() == True and player.getX_location() > viewport.offsetX:
        if(player.powerLevel == 1):
            player.updateImage(smallMario[1])
        elif(player.powerLevel == 2):
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
                sound_obj.play_sound("jump")
                player.setJumping(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.setMoveRight(False)
            if event.key == pygame.K_LEFT:
                player.setMoveLeft(False)
            if event.key == pygame.K_SPACE:
                player.setJumping(False)

    # Update sprites on screen
    viewport.render_sprites(player, enemy_list, block_list, pipe_list, flag_list, powerup_list, projectile_list)
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

        if isinstance(enemy, Enemy4):
            enemy.throw(-3, -15, projectile_list)

        if enemy.rect.y > lowestTile-5:
            enemy.kill()

        enemyTile = pygame.sprite.spritecollide(enemy, block_list, False)

        if len(enemyTile) > 0:
            for tile in enemyTile:
                enemy.collision[0] = tile.rect.collidepoint(enemy.rect.topleft)
                enemy.collision[1] = tile.rect.collidepoint(enemy.rect.midtop)
                enemy.collision[2] = tile.rect.collidepoint(enemy.rect.topright)
                enemy.collision[3] = tile.rect.collidepoint(enemy.rect.midleft)
                enemy.collision[4] = tile.rect.collidepoint(enemy.rect.center)
                enemy.collision[5] = tile.rect.collidepoint(enemy.rect.midright)
                enemy.collision[6] = tile.rect.collidepoint(enemy.rect.bottomleft)
                enemy.collision[7] = tile.rect.collidepoint(enemy.rect.midbottom)
                enemy.collision[8] = tile.rect.collidepoint(enemy.rect.bottomright)

                if enemy.speed > 0:
                    if enemy.collision[5]:
                        enemy.speed *= -1
                        enemy.move()
                
                if enemy.speed < 0:
                    if enemy.collision[3]:
                        enemy.speed *= -1
                        enemy.move()

    for projectile in projectile_list:
        projectile.move(SCREEN_HEIGHT, projectile_list)

    # detect collisions between enemies and blocks
    enemyGround = pygame.sprite.groupcollide(enemy_list, block_list, False, False)
    for enemy, blocks in enemyGround.items():
        if len(blocks) > 0:
            primary_block = blocks[0]
            enemy.gravity(primary_block.rect.y)

    # checks for standing on a block and continues gravity if not 
    playerGround = pygame.sprite.spritecollide(player, block_list, False)
    enemyHit = pygame.sprite.spritecollide(player, enemy_list, False)
    projectile_hit = pygame.sprite.spritecollide(player, projectile_list, False)

    player.touch(playerGround, block_list, powerup_list, enemy_list, level_info, sound_obj)

    if player.invincible <= 0:
        if player.enemyHit(enemyHit, sound_obj, level_info) and player.powerLevel == 1:
            player.powerLevel = 0
        elif player.enemyHit(enemyHit, sound_obj, level_info) and player.powerLevel > 1:
            player.powerUp(1)
            player.invincible = 90

        if len(projectile_hit) > 0 and player.powerLevel == 1:
            player.powerLevel = 0
        elif len(projectile_hit) > 0 and player.powerLevel > 1:
            player.powerUp(player.powerLevel-1)
            player.invincible = 90

    animation += 1
    player.invincible -= 1
    if animation >= 15:
        block_list.update()
        pygame.display.flip()
        animation = 0

    flagTouch = pygame.sprite.spritecollide(player, renders['flagpole'], False)

    if(flagTouch in renders['flagpole']):
        sound_obj.stop_bg()
        sound_obj.play_sound("victory")
        player, viewport, renders, block_list, enemy_list = playerWin(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH, level)
        sound_obj.start_bg()

    #If player is below lowest tile, kill them
    if(player.getY_location() > lowestTile+5):
        player.powerLevel = 0

    level_info.tick()

    # Player loses if timer runs out
    if level_info.time == 0:
        player.powerLevel = 0
        viewport.render_time_out()
        pygame.display.quit()
        pygame.quit()  # Stop pygame
        sys.exit()  # Stop script

    if player.powerLevel == 0:
        sound_obj.stop_bg()
        sound_obj.play_sound("death")
        player, viewport, renders, block_list, enemy_list = playerDeath(player, viewport, SCREEN_HEIGHT, SCREEN_WIDTH, level, level_info)
        sound_obj.start_bg()

    pygame.display.update()
    clock.tick(60)  # Keeps game at 60fps
