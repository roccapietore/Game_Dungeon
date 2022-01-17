class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        return self.obj


class Field:
    def __init__(self, field, unit, cols, rows):
        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows

    def cell(self, x, y):
        return self.field[y][x]

    def get_field(self):
        return self.field

    def unit_move(self, x, y):
        if self.cell(x, y).get_obj().get_terrain() == 'Key':
            self.unit.set_key()
            print('Теперь у Вас есть ключ')

        if self.cell(x, y).get_obj().get_terrain() == 'Trap':
            self.unit.get_damage(10)
            print(f'Ловушка! Осталось {self.unit.hp} хит-поинтов')

        if self.cell(x, y).get_obj().is_walkable():
            self.unit.set_coordinates(x, y)
        if not self.cell(x, y).get_obj().is_walkable():
            print('Нельзя перемещаться на эту ячейку')

        if self.cell(x, y).get_obj().get_terrain() == 'Door':
            #self.cell(x, y).get_obj().get_terrain().step_on(self.unit)
            print('Уровень пройден!')

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x, y-1)

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x, y+1)

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x+1, y)

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x-1, y)

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows


