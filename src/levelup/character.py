from levelup.position import Position
from levelup.direction import Direction
from levelup.gameMap import GameMap

class Character:
    name = ""
    current_position :Position = Position(-100,-100)
    map :GameMap = GameMap()

    def __init__(self, character_name):
        self.name = character_name

    def move(self, direction :Direction) -> None:
        self.current_position = self.map.calculate_new_position(
            self.current_position, direction)
    
    def enter_map(self, map :GameMap):
        self.map = map
        self.current_position = self.map.starting_position

