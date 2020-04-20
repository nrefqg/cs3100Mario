import pygame
import blocks
from blocks.mushroom import mushroom
import enemies


class Character(pygame.sprite.Sprite):
    """
    Class that allows sprite function of the player
    """

    def __init__(self, x, y):
        """
        Constructor for the player
        :param x: The horizontal position of the enemy's upper left corner (in pixels)
        :param y: The vertical position of the enemy's upper left corner (in pixels)
        """
        super().__init__()
        if type(x) is not int:
                raise ValueError("Argument x should be an int")
        if type(y) is not int:
                raise ValueError("Argument y should be an int")
        self.x = x
        self.y = y
        self.image = pygame.image.load('sprites/mariosmall.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collision = [False] * 9

        # initial momentum and movement values
        self.x_momentum = 0
        self.y_momentum = 0
        self.move_right = False
        self.move_left = False
        self.jump = False
        self.vertical_move = False
        self.ground = False

        # sets initial change in y to the initial height
        self.deltaY = self.y

        # used to determine if player ran off a ledge/block into open air
        self.standing = False

        #Determines the level of powerup the player has.  0 means the player is small, 1 is big player, 2 is the highest level. In classic mario 2 would be fireflower
        self.powerLevel = 0

    # Getter and setters for location variables
    def getX_location(self):
            return self.rect.x
    def setX_location(self, newX):
            self.rect.x = newX
    def getY_location(self):
            return self.rect.y
    def setY_location(self, newY):
            self.rect.y = newY

    # Getter and setters for movement variables
    def getMoveRight(self):
        return self.move_right
    def setMoveRight(self, boolVal):
        self.move_right = boolVal
    def getMoveLeft(self):
        return self.move_left
    def setMoveLeft(self, boolVal):
        self.move_left = boolVal
    def getX_momentum(self):
        return self.x_momentum
    def setX_momentum(self, x):
        self.x_momentum = x
    def getY_momentum(self):
        return self.y_momentum
    def setY_momentum(self, y):
        self.y_momentum = y
    def getVertical(self):
        return self.vertical_move
    def setVertical(self, boolVert):
        self.vertical_move = boolVert
        
    # Jumping and gravity functions
    def getJumping(self):
        return self.jump
    def setJumping(self, boolVal):
        self.jump = boolVal
        self.ground = boolVal
    # change in y value from where jump happened
    def getDeltaY(self):
        return self.deltaY
    def setDeltaY(self, delt):
        self.deltaY = delt
    def groundBlockContact(self, ground_blocks):
        """
        gives the player gravity for jumping
        :return: None
        """
        if len(ground_blocks) > 0:
            # check for horizontal block collisions
            if self.rect.right <= ground_blocks[0].rect.left and self.move_right == True:
                self.x_momentum = 0
                self.move_right = False
                self.rect.right = ground_blocks[0].rect.left - 1
            elif self.rect.left >= ground_blocks[0].rect.right and self.move_left == True:
                self.x_momentum = 0
                self.move_left = False
                self.rect.left = ground_blocks[0].rect.right + 1
            # check for vertical block collisions
            elif self.rect.bottom >= ground_blocks[0].rect.top and not self.vertical_move and not self.ground:
                # stop moving vertically
                self.y_momentum = 0
                self.deltaY = 0
                self.rect.bottom = ground_blocks[0].rect.top + 1
                self.ground = True
            elif self.rect.top <= ground_blocks[0].rect.bottom and self.vertical_move:
                self.y_momentum = 0
                self.deltaY = 141
                self.rect.top = ground_blocks[0].rect.bottom
        elif self.deltaY == 0:  # initiate falling since not on a block
            self.deltaY = 1

    # attempt at new collision function
    def touch(self, tile_list, block_list):
        if len(tile_list) > 0:
            for tile in tile_list: 
                self.collision[0] = tile.rect.collidepoint(self.rect.topleft)
                self.collision[1] = tile.rect.collidepoint(self.rect.midtop)
                self.collision[2] = tile.rect.collidepoint(self.rect.topright)
                self.collision[3] = tile.rect.collidepoint(self.rect.midleft)
                self.collision[4] = tile.rect.collidepoint(self.rect.center)
                self.collision[5] = tile.rect.collidepoint(self.rect.midright)
                self.collision[6] = tile.rect.collidepoint(self.rect.bottomleft)
                self.collision[7] = tile.rect.collidepoint(self.rect.midbottom)
                self.collision[8] = tile.rect.collidepoint(self.rect.bottomright)

                # tile is below player
                if (tile.rect.bottomright[1] > self.rect.bottomright[1]) or (tile.rect.bottomright[1] + 6 == self.rect.bottomright[1]):
                    if self.rect.bottom > tile.rect.top and not self.vertical_move:
                        # stop moving vertically
                        self.y_momentum = 0
                        self.deltaY = 0
                        self.rect.bottom = tile.rect.top + 6
                elif tile.rect.topright[1] < self.rect.topright[1]:
                    if self.rect.top <= tile.rect.bottom and self.vertical_move:
                        self.y_momentum = 0
                        self.deltaY = 141
                        self.rect.top = tile.rect.bottom
                        if isinstance(tile, blocks.breakableBlock.breakableBlock) and self.powerLevel > 0:
                            tile.kill()
                        if isinstance(tile, blocks.powerBlock.powerBlock):
                            print("power block hit")
                            tile.disabled(tile.rect.x, tile.rect.y)
                            print(type(tile))
                        if isinstance(tile, blocks.singleCoin.singleCoin):
                            print("Single Coin block")
                            tile.disabled(tile.rect.x, tile.rect.y)
                        if isinstance(tile, blocks.star.star):
                            print("star block")
                            tile.disabled(tile.rect.x, tile.rect.y)
                        if isinstance(tile, blocks.oneUp.oneUp):
                            print("oneUp block")
                            tile.disabled(tile.rect.x, tile.rect.y)
                        if isinstance(tile, blocks.multiCoin.multiCoin):
                            print("multiCoin block")
                            if not tile.decrementCount():
                                tile.disabled(tile.rect.x, tile.rect.y)
                        if isinstance(tile, blocks.hiddenBlock.hiddenBlock):
                            print("hidden block")
                            tile.disabled(tile.rect.x, tile.rect.y)
                # side collisions
                #if tile.rect.top > self.rect.bottom or tile.rect.bottom < self.rect.top:
                if self.collision[3] or self.collision[5]:
                    #if self.rect.right >= tile.rect.left and self.move_right:
                    if self.collision[5]:
                        self.rect.right = self.rect.right - self.x_momentum
                        self.x_momentum = 0
                        self.move_right = False
                    #elif self.rect.left <= tile.rect.right and self.move_left:
                    elif self.collision[3]:
                        self.rect.left = self.rect.left + self.x_momentum
                        self.x_momentum = 0
                        self.move_left = False
        elif self.deltaY == 0:
            self.deltaY = 1

    def touchPipe(self, tile_list):
        if len(tile_list) > 0:
            for tile in tile_list: 
                self.collision[0] = tile.rect.collidepoint(self.rect.topleft)
                self.collision[1] = tile.rect.collidepoint(self.rect.midtop)
                self.collision[2] = tile.rect.collidepoint(self.rect.topright)
                self.collision[3] = tile.rect.collidepoint(self.rect.midleft)
                self.collision[4] = tile.rect.collidepoint(self.rect.center)
                self.collision[5] = tile.rect.collidepoint(self.rect.midright)
                self.collision[6] = tile.rect.collidepoint(self.rect.bottomleft)
                self.collision[7] = tile.rect.collidepoint(self.rect.midbottom)
                self.collision[8] = tile.rect.collidepoint(self.rect.bottomright)

                # tile is below player
                if (tile.rect.bottomright[1] > self.rect.bottomright[1]) or (tile.rect.bottomright[1] + 6 == self.rect.bottomright[1]):
                    if self.rect.bottom > tile.rect.top and not self.vertical_move:
                        # stop moving vertically
                        self.y_momentum = 0
                        self.deltaY = 0
                        self.rect.bottom = tile.rect.top + 6 
                        if isinstance(tile, blocks.pipe.entrance):
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    o = 0 # Move to hidden level

                elif tile.rect.topright[1] < self.rect.topright[1]:
                    if self.rect.top <= tile.rect.bottom and self.vertical_move:
                        self.y_momentum = 0
                        self.deltaY = 141
                        self.rect.top = tile.rect.bottom
                        if isinstance(tile, blocks.breakableBlock.breakableBlock):
                            tile.kill()
                        if isinstance(tile, blocks.powerBlock.powerBlock):
                            print("power block hit")
                # side collisions
                #if tile.rect.top > self.rect.bottom or tile.rect.bottom < self.rect.top:
                if self.collision[3] or self.collision[5]:
                    #if self.rect.right >= tile.rect.left and self.move_right:
                    if self.collision[5]:
                        self.rect.right = self.rect.right - self.x_momentum
                        self.x_momentum = 0
                        self.move_right = False
                    #elif self.rect.left <= tile.rect.right and self.move_left:
                    elif self.collision[3]:
                        self.rect.left = self.rect.left + self.x_momentum
                        self.x_momentum = 0
                        self.move_left = False
        elif self.deltaY == 0:
            self.deltaY = 1

    def enemyHit(self, enemy_list):
        if len(enemy_list) > 0:
            for enemy in enemy_list:
                self.collision[0] = enemy.rect.collidepoint(self.rect.topleft)
                self.collision[1] = enemy.rect.collidepoint(self.rect.midtop)
                self.collision[2] = enemy.rect.collidepoint(self.rect.topright)
                self.collision[3] = enemy.rect.collidepoint(self.rect.midleft)
                self.collision[4] = enemy.rect.collidepoint(self.rect.center)
                self.collision[5] = enemy.rect.collidepoint(self.rect.midright)
                self.collision[6] = enemy.rect.collidepoint(self.rect.bottomleft)
                self.collision[7] = enemy.rect.collidepoint(self.rect.midbottom)
                self.collision[8] = enemy.rect.collidepoint(self.rect.bottomright)

                if self.collision[6] or self.collision[7] or self.collision[8]:
                    self.setJumping(True)
                    enemy.kill()

                else:
                    return True
                    

    #This code will drive upgrading the player when a powerup is collected, or will shrink the player if they are damaged.
    def powerUp(self, power):
        if power == 0:
            self.powerLevel = 0
            temp = self.rect.bottomleft
            self.image = pygame.image.load('sprites/mariosmall.png')
            self.rect = self.image.get_rect()
            self.rect.bottomleft = temp
        elif power == 1:
            temp = self.rect.bottomleft
            self.powerLevel = 1
            self.image = pygame.image.load('sprites/mariobig.png')
            self.rect = self.image.get_rect()
            self.rect.bottomleft = temp
        elif power == 2:
            self.powerLevel = 2
            temp = self.rect.bottomleft
            self.image = pygame.image.load('sprites/mariopower.png')
            self.rect = self.image.get_rect()
            self.rect.bottomleft = temp
    # image update functions
    def updateImage(self, file):
        self.image = pygame.image.load(file)
