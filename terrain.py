from unit import Unit


class Terrain:
    def __init__(self, walkable, terrain):
        self.walkable = walkable
        self.terrain = terrain
        self.unit = None

    def step_on(self, unit):
        self.unit = unit

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain


class Door(Terrain):
    def __init__(self):
        super().__init__(walkable=True, terrain="Door")

    def step_on(self, unit):
        if unit.has_key() is True:
            unit.escaped = True
            return True


class Key(Terrain):
    def __init__(self):
        super().__init__(walkable=True, terrain="Key")

    def step_on(self, unit: Unit):
        return unit.set_key()


class Trap(Terrain):
    def __init__(self, damage):
        super().__init__(walkable=True, terrain="Trap")
        self.damage = damage

    def step_on(self,  unit: Unit):
        unit.get_damage(self.damage)


class Grass(Terrain):
    def __init__(self):
        super().__init__(walkable=True, terrain="Grass")


class Wall(Terrain):
    def __init__(self):
        super().__init__(walkable=False, terrain="Wall")
