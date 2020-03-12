import pygame
import os


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
            raise ValueError("Argument name should be a string")
        if type(x) is not int:
            raise ValueError("Argument x should be an int")
        if type(y) is not int:
            raise ValueError("Argument y should be an int")

        self.image = image
        self.x = x
        self.y = y
        self.position = 0
        self.speed = 0

        self.image = pygame.image.load(os.path.join('enemies', 'sprites', image))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def destroy(self, sprite_group):
        """
        Destroys the enemy sprite from the given sprite group
        :param sprite_group: The Group the Enemy belongs to
        :return: None
        """
        sprite_group.remove(self)
