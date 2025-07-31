# https://github.com/GarrettUrso/lab10-GU-KV
# Partner 1: Garrett Urso
# Partner 2: Kirk Andrew Vinas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,6), 7)
        self.assertEqual(add(0,6), 6)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(1, 6), -5)
        self.assertEqual(sub(0, 6), -6)
        self.assertEqual(sub(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 0.2)
        self.assertAlmostEqual(div(7, 3), 0.42857142857142855, places=6)
        self.assertEqual(div(3, -9), -3)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,10), 1)
        self.assertAlmostEqual(logarithm(10,20),1.30102999, places=5 )
        self.assertEqual(logarithm(50,50), 1)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
        self.assertEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(2), 1.4142135, places=6)
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()