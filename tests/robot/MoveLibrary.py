from levelup.controller import GameController
from levelup.controller import Direction

class MoveLibrary:
    start_x: int
    start_y: int
    move_count: int
    controller = GameController()

    def initialize_character_xposition_with(self, x_position):
        self.start_x = int(x_position)

    def initialize_character_yposition_with(self, y_position):
        self.start_y = int(y_position)

    def initialize_character_movecount_with(self, move_count):
        self.move_count = int(move_count)

    def move_in_direction(self, direction):
        self.controller.initalize_game_for_testing()
        self.controller.set_current_move_count(self.move_count)
        self.controller.set_character_position((self.start_x, self.start_y))


        print("POSITION" + str(self.controller.status.current_position))

        direction_mapped = None
        if(direction == "NORTH"):
            direction_mapped = Direction.NORTH
        elif(direction == "SOUTH"):
            direction_mapped = Direction.SOUTH
        elif(direction == "EAST"):
            direction_mapped = Direction.EAST
        else:
            direction_mapped = Direction.WEST

        self.controller.move(direction_mapped)

        print("POSITION" + str(self.controller.status.current_position))
    

    def character_xposition_should_be(self, expected):
        end_x = self.controller.status.current_position[0]
        assert end_x == int(expected), f"Expected end x: {expected}, Actual end x: {end_x}"

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.current_position[1]
        assert end_y == int(expected), f"Expected end y: {expected}, Actual end y: {end_y}"

    def character_movecount_should_be(self, expected):
        actual = self.controller.status.move_count
        assert actual == int(expected), f"Expected: {expected}, Actual: {actual}"
