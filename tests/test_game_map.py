from unittest import TestCase
from levelup.gameMap import GameMap

class TestGameMap(TestCase):
    def test_number_of_positions(self):
        # Create an instance of the GameMap
        gameMap = GameMap()
        
        # Call the method that returns the number of positions
        num_positions = gameMap.num_positions
        
        # Check if the number of positions is 100
        self.assertEqual(num_positions, 100, "Number of positions should be 100")

