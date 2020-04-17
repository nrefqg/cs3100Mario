import pygame


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
        self.image = pygame.image.load('sprites/mario.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # initial momentum and movement values
        self.x_momentum = 0
        self.y_momentum = 0
        self.move_right = False
        self.move_left = False
        self.jump = False
        self.vertical_move = False

        # sets initial change in y to the initial height
        self.deltaY = self.y

        # used to determine if player ran off a ledge/block into open air
        self.standing = False

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
            for block in ground_blocks:
                if self.rect.right < block.rect.left and self.move_right == True:
                    self.x_momentum = 0
                    self.move_right = False
                    self.rect.right = block.rect.left
                elif self.rect.left > block.rect.right and self.move_left == True:
                    self.x_momentum = 0
                    self.move_left = False
                    self.rect.left = block.rect.right
                # check for vertical block collisions
                elif self.rect.bottom >= block.rect.top and not self.vertical_move:
                    self.y_momentum = 0
                    self.deltaY = 0
                    self.rect.bottom = block.rect.top + 6  # +6 fixes photo placement
                elif self.rect.top <= block.rect.bottom and self.vertical_move:
                    self.y_momentum = 0
                    self.deltaY = 141
                    self.rect.top = block.rect.bottom
        elif self.deltaY == 0:   # initiate falling since not on a block
            self.deltaY = 1

    # image update functions
    def updateImage(self, file):
        self.image = pygame.image.load(file)

