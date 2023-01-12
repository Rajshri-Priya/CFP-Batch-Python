import unittest

def square(x):
    return x * x

class TestSquare(unittest.TestCase):
    def test_square_of_5(self):
        self.assertEqual(square(5), 25)

    def test_square_of_4(self):
        self.assertEqual(square(4), 16)

    def test_square_of_negative_2(self):
        self.assertEqual(square(-2), 4)

if __name__ == '__main__':
    unittest.main()
