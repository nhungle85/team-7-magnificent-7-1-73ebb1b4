from unittest import TestCase
from levelup.character import *
from levelup.gameMap import *
class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

  
    def test_is_valid_name(self):
        ARBITRARY_NAME = "MyName@"
        expected = is_valid_name(ARBITRARY_NAME)
       
        self.assertFalse(expected)

    def test_valid_moves(self):
        my_map = GameMap(10, 10)
        # my_map.move(5, 5)
        self.assertEqual(my_map.position, (5, 5))
        # my_map.move(9, 9)
        # self.assertEqual(my_map.position, (9, 9))


