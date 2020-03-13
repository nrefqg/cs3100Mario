import pygame
import os
from enemies.enemy import Enemy


class Enemy1(Enemy):
    """
    Enemy type 1 (lateral movement with stunned state)
    """

    def __init__(self, x, y, speed):
        """
        Constructor for Enemy1
        :param x: The horizontal position of the enemy's upper left corner (in pixels)
        :param y: The vertical position of the enemy's upper left corner (in pixels)
        :param speed: The speed of the enemy (negative is left, positive is right)
        """
        super().__init__("koopa.png", x, y)
        self.speed = speed
        self.dx = speed
        self.health = 2
        self.regen = 0

    def move(self):
        """
        Move Enemy1
        :return: None
        """
        super().move()
        distance = 150

        if self.regen > 0:
            self.regen -= 1
            if self.regen == 0:
                self.respawn()
            return  # do not move while regenerating

        if 0 <= self.position <= distance:  # use of distance for testing purposes only
            self.rect.x += self.speed
        elif distance <= self.position <= 2 * distance:
            self.rect.x -= self.speed
        else:
            self.position = 0

        self.position += 1

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
            else:  # enemy is in the stunned state, so change sprite and stop moving during regen period
                self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'koopa-shell.png'))
                self.dx = self.speed
                self.speed = 0
                self.regen = 300

    def respawn(self):
        """
        Respawn the enemy to its initial state and health
        :return: None
        """
        self.health = 2
        self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'koopa.png'))
        self.speed = self.dx

    def flip(self):
        """
        Flip Enemy1 in the opposite direction as long as it is not in the stunned state
        :return: None
        """
        if self.health == 2:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
