from enemies.enemy import Enemy


class Enemy0(Enemy):
    """
    Enemy type 0 (lateral movement only)
    """

    def __init__(self, x, y, speed):
        """
        Constructor for Enemy0
        :param x: The horizontal position of the enemy's upper left corner (in pixels)
        :param y: The vertical position of the enemy's upper left corner (in pixels)
        :param speed: The speed of the enemy (negative is left, positive is right)
        """
        super().__init__("goomba.png", x, y)
        self.speed = speed

    def move(self):
        """
        Move Enemy0
        :return: None
        """
        super().move()
        distance = 200

        if 0 <= self.position <= distance:  # use of distance for testing purposes only
            self.rect.x += self.speed
        elif distance <= self.position <= 2 * distance:
            self.rect.x -= self.speed
        else:
            self.position = 0

        self.position += 1

    def flip(self):
        """
        Flip Enemy0 in the opposite direction by reversing speed
        :return: None
        """
        self.speed *= -1
