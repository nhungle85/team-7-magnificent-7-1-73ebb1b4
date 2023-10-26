from unittest import TestCase
from levelup.gameMap import GameMap

class TestGameMap(TestCase):

    def test_number_of_positions(self):
        # Create an instance of the GameMap
        game_map = GameMap()
        
        # Call the method that returns the number of positions
        num_positions = game_map.num_positions
        
        # Check if the number of positions is 100
        self.assertEqual(num_positions, 100, "Number of positions should be 100")



    def test_validate_position(self):
        my_map = GameMap(10, 10)
        
        resultTrue = my_map.validate_postion(5, 5)
        self.assertTrue(resultTrue)

        resultFalse = my_map.validate_postion(11, 11)
        self.assertFalse(resultFalse)


