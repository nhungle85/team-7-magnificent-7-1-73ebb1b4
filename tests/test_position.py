from unittest import TestCase
from levelup.position import *



class TestGetPosition(TestCase):
    def test_valid_positions(self):
        
        actual = Position.getPosition(0, 0)
        self.assertEqual((0, 0), actual)
        self.assertEqual(Position.getPosition(5, 5), (5, 5))
        self.assertEqual(Position.getPosition(9, 9), (9, 9))

    def test_invalid_positions_x(self):
        self.assertIsNone(Position.getPosition(-1, 5))
        self.assertIsNone(Position.getPosition(10, 5))

    def test_invalid_positions_y(self):
        self.assertIsNone(Position.getPosition(5, -1))
        self.assertIsNone(Position.getPosition(5, 10))

    if __name__ == '__main__':
        unittest.main()
