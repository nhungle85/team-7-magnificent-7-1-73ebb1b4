import logging
from dataclasses import dataclass
from enum import Enum
from levelup.character import Character
from levelup.direction import Direction
from levelup.gameMap import GameMap
from levelup.position import Position


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (0,0)
    move_count: int = 0


class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:

    character: Character

    status: GameStatus
    map:GameMap
    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        self.map = GameMap()
        if self.character == None:
            self.create_character(DEFAULT_CHARACTER_NAME)
        self.character.enter_map(self.map)
        self.status.running = True
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = 0
    
    def initalize_game_for_testing(self) -> None:
        self.create_character("")
        self.start_game()

    def update_status(self,position_x, position_y, move_count) -> None:
        self.status.current_position = (position_x, position_y)
        self.status.move_count = move_count

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.character = Character(character_name)
        else:
            self.character = Character(DEFAULT_CHARACTER_NAME)
        self.status.character_name = self.character.name


    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        self.status.current_position = (self.character.current_position.x, self.character.current_position.y)
        self.status.move_count = self.status.move_count + 1

    def set_character_position(self, xycoordinates: tuple) -> None:
        x = xycoordinates[0]
        y = xycoordinates[1]
        self.character.current_position = Position(x,y)
        self.status.current_position = xycoordinates

    def set_current_move_count(self, move_count: int) -> None:
        self.status.move_count = move_count

    def get_total_positions(self) -> int:
        return self.map.size[0]*self.map.size[1]
    
