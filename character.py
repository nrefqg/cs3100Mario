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

                self.deltaY = self.y

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

        # Jumping and gravity functions
        def getJumping(self):
                return self.jump
        def setJumping(self, boolVal):
                self.jump = boolVal
        def groundContact(self, ground):
                """
                gives the player gravity for jumping
                :return: None
                """
                # check if passed the ground
                if self.rect.y + self.rect.height >= ground and self.y_momentum >= 0:
                        # stop moving vertically
                        self.y_momentum = 0
                        self.deltaY = 0

                        # reset rect to be above ground
                        #self.rect.y = ground - self.rect.height

        # image update functions
        def updateImage(self, file):
                self.image = pygame.image.load(file)

        # test jumping functions using delta variables
        # versus using hard coded pixel values
        def getDeltaY(self):
                return self.deltaY
        def setDeltaY(self, delt):
                self.deltaY = delt

