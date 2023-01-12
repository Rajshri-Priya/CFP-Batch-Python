# testing for prime_no fxn

import unittest

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

class TestIsPrime(unittest.TestCase):
    def test_is_prime_5(self):
        self.assertTrue(is_prime(5))

    def test_is_prime_4(self):
        self.assertFalse(is_prime(4))
        
    def test_is_prime_0(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_1(self):
        self.assertFalse(is_prime(1))
        
if __name__ == '__main__':
    unittest.main()
