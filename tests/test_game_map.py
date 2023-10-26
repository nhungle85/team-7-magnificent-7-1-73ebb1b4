from unittest import TestCase
from levelup.gameMap import GameMap

class TestGameMap(TestCase):
    def test_init_creates_positions(self):
        testobj = GameMap()
        self.assertNotEqual(None, testobj.positions)
        self.assertEqual(10, len(testobj.positions))



