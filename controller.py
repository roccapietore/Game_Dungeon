class GameController:
    def __init__(self, game_on, hero, field):
        self.mapping = {
            'Wall': '🔲',
            'Grass': '⬜️',
            'Ghost': '👻',
            'Key': '🗝',
            'Door': '🚪',
            'Trap': '💀',
        }

        self.game_on = game_on
        self.hero = hero
        self.game_on = game_on
        self.field = field

    def make_field(self):
        return

    def play(self):
        while not self.unit.has_key():
            command = input()
            if command == "w":
                self.field.move_unit_up()
            elif command == "s":
                self.field.move_unit_down()
            elif command == "a":
                self.field.move_unit_left()
            elif command == "d":
                self.field.move_unit_right()
            elif command == "stop" or "exit":
                break
