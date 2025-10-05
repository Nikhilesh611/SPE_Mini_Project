import unittest
from scientific_calculator import calc
import math

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(calc.square_root(25), 5)
        self.assertAlmostEqual(calc.square_root(2), 1.4142, places=4)
        with self.assertRaises(ValueError):
            calc.square_root(-9)

    def test_factorial(self):
        self.assertEqual(calc.factorial(5), 120)
        self.assertEqual(calc.factorial(0), 1)
        with self.assertRaises(ValueError):
            calc.factorial(-3)

    def test_natural_log(self):
        self.assertAlmostEqual(calc.natural_log(1), 0.0, places=4)
        self.assertAlmostEqual(calc.natural_log(math.e), 1.0, places=4)
        with self.assertRaises(ValueError):
            calc.natural_log(0)
        with self.assertRaises(ValueError):
            calc.natural_log(-10)

if __name__ == "__main__":
    unittest.main()
