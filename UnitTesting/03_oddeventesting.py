# testing for fxn even ()

import unittest

def check_even(number):
    if number % 2 == 0:
        return True
    return False

class TestCheckEven(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(check_even(2))
        self.assertTrue(check_even(4))
        self.assertTrue(check_even(200))
        self.assertTrue(check_even(100))

    def test_odd_numbers(self):
        self.assertFalse(check_even(1))
        self.assertFalse(check_even(3))
        self.assertFalse(check_even(101))
        self.assertFalse(check_even(111))

if __name__ == '__main__':
    unittest.main()
