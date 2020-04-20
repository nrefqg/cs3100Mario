import pygame
import os

GRAVITY = 0.5


class Projectile(pygame.sprite.Sprite):
    """
    A projectile that can damage the player
    """

    def __init__(self, x, y, x_speed, y_speed):
        """
        Constructor for a Projectile
        :param x: The initial horizontal position of the projectile
        :param y: The initial vertical position of the projectile
        :param x_speed The horizontal speed of the projectile (constant)
        :param y_speed The initial vertical speed of the projectile (changed by gravity)
        """
        super().__init__()
        self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'projectile.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self, screen_height, projectile_group):
        """
        Moves the projectile vertically with gravity and horizontally
        :return: None
        """

        if self.rect.y + self.rect.height >= screen_height:
            projectile_group.remove(self)  # remove from screen if it falls offscreen
        else:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            self.y_speed += GRAVITY
