from enemies.enemy import Enemy


class Enemy0(Enemy):

    def __init__(self, x, y, speed):
        super().__init__("goomba.png", x, y)
        self.speed = speed

    def move(self):
        distance = 100

        if 0 <= self.position <= distance:
            self.rect.x += self.speed
        elif distance <= self.position <= 2 * distance:
            self.rect.x -= self.speed
        else:
            self.position = 0

        self.position += 1

    def flip(self):
        self.speed *= -1
