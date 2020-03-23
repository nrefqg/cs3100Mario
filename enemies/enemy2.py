import pygame
import os
from enemies.enemy import Enemy


class Enemy2(Enemy):
    """
    Enemy type 2 (lateral movement, jumping, behaves like Enemy1 after one hit)
    """

    def __init__(self, x, y, speed):
        """
        Constructor for Enemy2
        :param x: The horizontal position of the enemy's upper left corner (in pixels)
        :param y: The vertical position of the enemy's upper left corner (in pixels)
        :param speed: The speed of the enemy (negative is left, positive is right)
        """
        super().__init__("flying-parakoopa.png", x, y)
        self.speed = speed
        self.dx = speed
        self.health = 3
        self.regen = 0

    def move(self):
        """
        Move Enemy2, or wait for regen
        :return: None
        """
        super().move()

        if self.regen > 0:
            self.regen -= 1
            if self.regen == 0:
                self.respawn()
            return  # do not move/jump while regenerating

        self.rect.x += self.speed
        if self.health == 3:
            self.jump(4)

    def damage(self, group):
        """
        Deal one unit of damage to this enemy, and change state accordingly
        :param group: The sprite group the enemy belongs to
        :return: None
        """
        if self.health > 0:
            self.health -= 1  # deduct one health point
            if self.health == 0:
                self.destroy(group)  # destroy this enemy if the health reaches 0
            elif self.health == 1:  # enemy is in stunned state, so change sprite and stop moving during regen period
                self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'parakoopa-shell.png'))
                self.dx = self.speed
                self.speed = 0
                self.regen = 300
            elif self.health == 2:  # enemy can no longer jump
                self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'parakoopa.png'))

    def respawn(self):
        """
        Respawn the enemy to its initial state and health
        :return: None
        """
        self.health = 2
        self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'flying-parakoopa.png'))
        self.speed = self.dx

    def flip(self):
        """
        Flip Enemy2 in the opposite direction as long as it is not in the stunned state
        :return: None
        """
        if self.health > 1:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
