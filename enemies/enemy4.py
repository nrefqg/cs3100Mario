import pygame
from enemies.enemy import Enemy
from enemies.projectile import Projectile


class Enemy4(Enemy):
    """
    Enemy type 4 (jumps and throws hammers to attack)
    """

    def __init__(self, x, y, speed):
        """
        Constructor for Enemy4
        :param x: The horizontal position of the enemy's upper left corner (in pixels)
        :param y: The vertical position of the enemy's upper left corner (in pixels)
        :param speed: The speed of the enemy (negative is left, positive is right)
        """
        super().__init__("hammerbro.png", x, y)
        self.speed = speed
        self.dx = speed
        self.health = 1
        self.throw_delay = 0
        self.jump_delay = 0

    def move(self):
        """
        Move Enemy4 and throw hammers
        :return: None
        """
        super().move()

        if self.health == 0:
            return

        if self.jump_delay == 0:
            self.jump(15)
            self.jump_delay = 150
        else:
            self.jump_delay -= 1  # count down to next jump

    def throw(self, x_speed, y_speed, projectile_group):
        """
        Throws a projectile with an initial vertical speed
        :param x_speed: Constant horizontal speed (negative is left, positive is right)
        :param y_speed: Initial vertical speed (negative is up, positive is down)
        :return: None
        """
        if self.throw_delay == 0:
            self.throw_delay = 100
            new_projectile = Projectile(self.rect.x, self.rect.y, x_speed, y_speed)
            projectile_group.add(new_projectile)
        else:
            self.throw_delay -= 1  # count down to next throw

    def flip(self):
        """
        Flip Enemy4 in the opposite direction
        :return: None
        """
        self.speed *= -1
        self.image = pygame.transform.flip(self.image, True, False)


