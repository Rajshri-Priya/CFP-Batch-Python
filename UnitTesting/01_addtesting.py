# testing for add method
import unittest
from addfxn import *


class TestAddFunction(unittest.TestCase):
    def test_add_int(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = add(10.5, 20.5)
        self.assertEqual(result, 31.0)

    def test_add_strings(self):
        result = add("Hello, ", "world")
        self.assertEqual(result, "Hello, world")


if __name__ == '__main__':
    unittest.main()
