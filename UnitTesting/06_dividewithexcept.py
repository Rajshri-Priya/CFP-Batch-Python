# testing on divide with exception handling

import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

class TestDivideFunction(unittest.TestCase):
    def test_divide_integers(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError): # an exception of the specified type is not raised inside the with block, the test will fail. 
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
