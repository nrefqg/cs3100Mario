from hitbox import Hitbox


class Enemy:

    def __init__(self, name, hitbox):
        if type(name) is not str:
            raise ValueError("Argument name should be a string")
        if not isinstance(hitbox, Hitbox):
            raise ValueError("Argument hitbox should be a Hitbox object")
        self._name = name
        self._hitbox = hitbox
