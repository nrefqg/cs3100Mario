from enemy import Enemy


class Enemy1(Enemy):

    def __init__(self, x, y):
        super().__init__("goomba.png", x, y)

    def move(self, speed):
        distance = 100

        if 0 <= self.position <= distance:
            self.rect.x += speed
        elif distance <= self.position <= 2 * distance:
            self.rect.x -= speed
        else:
            self.position = 0

        self.position += 1
