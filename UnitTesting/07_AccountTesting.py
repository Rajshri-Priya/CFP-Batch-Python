
import unittest
from ClassAccount import *


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account(100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)
        self.assertEqual(self.account.deposit(20), 170)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(50), 50)
        self.assertEqual(self.account.withdraw(60), -10)

    def test_withdraw_with_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == '__main__':
    unittest.main()
