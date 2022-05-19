import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculated_value = Calculator.add(3, 2)
        expected_value = 5
        self.assertEqual(calculated_value, expected_value)

    def test_sub(self):
        calculated_value = Calculator.sub(3, 2)
        expected_value = 1
        self.assertEqual(calculated_value, expected_value)

    def test_mul(self):
        calculated_value = Calculator.mul(3, 2)
        expected_value = 6
        self.assertEqual(calculated_value, expected_value)

if __name__ == '__main__':
    unittest.main()
