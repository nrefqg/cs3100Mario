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
        self.score = 100

    def move(self):
        """
        Move Enemy0
        :return: None
        """
        super().move()
        self.rect.x += self.speed

    def flip(self):
        """
        Flip Enemy0 in the opposite direction by reversing speed
        :return: None
        """
        self.speed *= -1

    def damage(self, group, level):
        self.destroy(group, level)
