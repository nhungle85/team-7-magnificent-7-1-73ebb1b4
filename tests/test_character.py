from unittest import TestCase
from levelup.character import *

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

  
    def test_is_valid_name(self):
        ARBITRARY_NAME = "MyName@"
        expected = is_valid_name(ARBITRARY_NAME)
       
        self.assertFalse(expected)
