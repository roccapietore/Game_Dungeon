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

    def cell(self):
        return self.unit.get_coordinates()

    def get_field(self):
        return self.field

    def move_unit_up(self):
        return self.unit.set_coordinates(x=self.x, y=self.y+1)

    def move_unit_down(self):
        return self.unit.set_coordinates(x=self.x, y=self.y-1)

    def move_unit_right(self):
        return self.unit.set_coordinates(x=self.x+1, y=self.y)

    def move_unit_left(self):
        return self.unit.set_coordinates(x=self.x-1, y=self.y)

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows


