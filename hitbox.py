class Hitbox:

    def __init__(self, x1, y1, x2, y2):
        if not all(type(i) is int for i in [x1, y1, x2, y2]):
            raise ValueError("Hitbox arguments must be ints")

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, value):
        self._x1 = value

    @property
    def y1(self):
        return self._y1

    @y1.setter
    def y1(self, value):
        self._y1 = value

    @property
    def x2(self):
        return self._x2

    @x2.setter
    def x2(self, value):
        self._x2 = value

    @property
    def y2(self):
        return self._y2

    @y2.setter
    def y2(self, value):
        self._y2 = value

    @property
    def top_left(self):
        return self._x1, self._y1

    @top_left.setter
    def top_left(self, coordinate):
        if type(coordinate) is not tuple:
            raise ValueError("Coordinate should be a tuple")
        if len(coordinate) != 2:
            raise ValueError("Coordinate should have x and y value")
        self._x1 = coordinate[0]
        self._y1 = coordinate[1]

    @property
    def bottom_right(self):
        return self._x2, self._y2

    @bottom_right.setter
    def bottom_right(self, coordinate):
        if type(coordinate) is not tuple:
            raise ValueError("Coordinate should be a tuple")
        if len(coordinate) != 2:
            raise ValueError("Coordinate should have x and y value")
        self._x2 = coordinate[0]
        self._y2 = coordinate[1]