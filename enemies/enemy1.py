import pygame
import os
from enemies.enemy import Enemy


class Enemy1(Enemy):

    def __init__(self, x, y, speed):
        super().__init__("koopa.png", x, y)
        self.speed = speed
        self.dx = speed
        self.health = 2
        self.regen = 0

    def move(self):
        distance = 150

        if self.regen > 0:
            self.regen -= 1
            if self.regen == 0:
                self.respawn()
            return  # do not move while regenerating

        if 0 <= self.position <= distance:
            self.rect.x += self.speed
        elif distance <= self.position <= 2 * distance:
            self.rect.x -= self.speed
        else:
            self.position = 0

        self.position += 1

    def damage(self, group):
        if self.health > 0:
            self.health -= 1
            if self.health == 0:
                group.remove(self)
            else:
                self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'koopa-shell.png'))
                self.dx = self.speed
                self.speed = 0
                self.regen = 300

    def respawn(self):
        self.health = 2
        self.image = pygame.image.load(os.path.join('enemies', 'sprites', 'koopa.png'))
        self.speed = self.dx

    def flip(self):
        if self.health == 2:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image, True, False)
