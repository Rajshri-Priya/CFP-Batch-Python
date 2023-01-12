
import unittest
from CarClass import *

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("audi", "a4", 2022)

    def test_get_name(self):
        self.assertEqual(self.car.get_name(), "2022 Audi A4")

    def test_update_odometer(self):
        self.car.update_odometer(20)
        self.assertEqual(self.car.read_odometer(), 20)

    def test_update_odometer_with_rollback(self):
        self.car.update_odometer(20)
        self.car.update_odometer(10)
        self.assertEqual(self.car.read_odometer(), 20)

if __name__ == '__main__':
    unittest.main()
