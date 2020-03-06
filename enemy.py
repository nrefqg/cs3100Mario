import pygame
import os


class Enemy(pygame.sprite.Sprite):

    def __init__(self, image, x, y):
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

        self.image = pygame.image.load(os.path.join('sprites', image))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
