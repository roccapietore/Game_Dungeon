from exceptions import UnitDied


class Unit:
    def __init__(self, hp, got_key, coord):
        self.hp = hp
        self.got_key = got_key
        self.coord = coord
        self.escaped = False

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        return self.escaped

    def is_alive(self):
        if self.hp <= 0:
            return UnitDied
        return True

    def get_damage(self, damage):
        self.hp -= damage
        self.is_alive()

    def set_coordinates(self, x, y):
        self.coord = (x, y)

    def get_coordinates(self):
        return self.coord


"""
    def has_position(self):
        return self.??   
"""


class Ghost(Unit):
    def __init__(self, hp, coord):
        super().__init__(hp, coord)
        self.name = "Ghost"
