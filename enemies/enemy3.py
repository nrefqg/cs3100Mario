import pygame
import os
from enemies.enemy import Enemy


class Enemy3(Enemy):
    """
    Enemy type 3 (lateral movement with stunned, invulnerable state)
    """

    def __init__(self, x, y, speed):
        """
        Constructor for Enemy3
        :param x: The horizontal position of the enemy's upper left corner (in pixels)
        :param y: The vertical position of the enemy's upper left corner (in pixels)
        :param speed: The speed of the enemy (negative is left, positive is right)
        """
        super().__init__("beetle.png", x, y)
        self.speed = speed
        self.dx = speed
        self.health = 2
        self.regen = 0
        self.score = 500

    def move(self):
        """
        Move Enemy3, or wait for regen
        :return: None
        """
        super().move()

        if self.regen > 0:
            self.regen -= 1
            if self.regen == 0:
                self.respawn()
            return  # do not move while regenerating

        self.rect.x += self.speed

    def damage(self, group, level):
        """
        Deal one unit of damage to this enemy, and change state accordingly
        :param group: The sprite group the enemy belongs to
        :return: None
        """
        if self.invincibility > 0:
            self.invincibility -= 1

        if self.health > 1 and self.invincibility == 0:  # normal damage should not destroy enemy
            self.health -= 1
            if self.health == 0:
                self.destroy(group, level)
            else:  # enemy is in the stunned state, so change sprite and stop moving during regen period
                self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'beetle-shell.png'))
                self.dx = self.speed
                self.speed = 0
                self.regen = 300
                self.invincibility = 20

    def respawn(self):
        """
        Respawn the enemy to its original state and health
        :return: None
        """
        self.health = 2
        self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'beetle.png'))
        self.speed = self.dx

    def flip(self):
        """
        Flip Enemy3 in the opposite direction as long as it is not in the stunned state
        :return: None
        """
        if self.health == 2:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
