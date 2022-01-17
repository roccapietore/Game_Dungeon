from field import Cell
from functions import read_file
from unit import Unit, Ghost
from terrain import Grass, Key, Door, Trap, Wall
from field import Field


class GameController:
    def __init__(self):
        self.mapping = {
            'Wall': '🔳',
            'Grass': '⬜️',
            'Ghost': '👻',
            'Key': '🗝',
            'Door': '🚪',
            'Trap': '💀',
        }

        self.game_on = True
        self.hero = Unit
        self.field = None

    def make_field(self):
        fields = []
        file = read_file('fields_scheme.txt')
        row = len(file)
        col = len(file[0])

        for num, line in enumerate(file):
            field_line = []
            for item_num, item in enumerate(line.strip("\n")):
                if item == "W":
                    field_line.append(Cell(Wall()))
                if item == "g":
                    field_line.append(Cell(Grass()))
                if item == "G":
                    field_line.append(Cell(Grass()))
                    self.hero = Ghost(50, item_num, num)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap(10)))
            fields.append(field_line)

            self.field = Field(fields, self.hero, col, row)

    def _draw_field(self):
        for y, line in enumerate(self.field.get_field()):
            s = ""
            for x, item in enumerate(line):
                if self.hero.has_position(x, y):
                    s += self.mapping["Ghost"]
                else:
                    s += self.mapping[item.get_obj().get_terrain()]
            print(s)

    def play(self):
        self.make_field()
        while self.game_on:  #and self.hero.has_escaped is False:

            self._draw_field()
            command = input().lower()

            if command == "w":
                self.field.move_unit_up()
            elif command == "s":
                self.field.move_unit_down()
            elif command == "a":
                self.field.move_unit_left()
            elif command == "d":
                self.field.move_unit_right()
            elif command in ["stop", "exit"]:
                print("Конец игры")
                self.game_on = False
            else:
                print("Введи другую команду")

