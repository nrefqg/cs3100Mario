import pygame
import os

GRAVITY = 0.5


class Enemy(pygame.sprite.Sprite):
    """
    Superclass for defining common functionality of different enemy types
    """

    def __init__(self, image, x, y):
        """
        Constructor for an enemy
        :param image: The name of the sprite for the enemy as a string
        :param x: The horizontal position of the enemy's upper left corner (in pixels)
        :param y: The vertical position of the enemy's upper left corner (in pixels)
        """
        super().__init__()
        if type(image) is not str:
            raise ValueError("Argument image should be a string")
        if type(x) is not int:
            raise ValueError("Argument x should be an int")
        if type(y) is not int:
            raise ValueError("Argument y should be an int")

        self.image = image
        self.x = x
        self.y = y
        self.speed = 0
        self.yspeed = 0
        self.is_jumping = False
        self.can_jump = False

        self.image = pygame.image.load(os.path.join('enemies', 'sprites', image))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.collision = [False] * 9
    def destroy(self, sprite_group):
        """
        Destroys the enemy sprite from the given sprite group
        :param sprite_group: The Group the Enemy belongs to
        :return: None
        """
        sprite_group.remove(self)

    def move(self):
        """
        Abstracted method for moving enemy sprites
        :return:
        """
        if self.yspeed != 0:
            self.rect.y += self.yspeed  # cause sprite to fall

    def gravity(self, ground):
        """
        Applies gravity to the enemy with respect to a specified ground
        :param ground: the height (in pixels) that the ground is at
        :return: None
        """
        if self.rect.y + self.rect.height >= ground and self.yspeed >= 0:  # check if passed the ground
            self.can_jump = True
            self.yspeed = 0  # stop moving vertically
            self.rect.y = ground - self.rect.height + 1  # reset rect to be above ground
        else:
            self.can_jump = False
            self.yspeed += GRAVITY  # accelerate due to gravity

    def jump(self, speed):
        """
        Causes the enemy to jump
        :param speed: the initial speed of the jump
        :return: None
        """
        if self.yspeed == 0 and self.can_jump:  # can only jump if not falling
            self.is_jumping = True
            self.yspeed -= speed  # causes sprite to jump (in -y direction)
