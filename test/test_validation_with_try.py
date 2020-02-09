import unittest

from input_validation.validation_with_try import average


def test_average_exception1(self):
    with self.assertRaises(ValueError):
        average(-90, 89, 78)


def test_average_exception2(self):
    with self.assertRaises(ValueError):
        average(90, -89, 78)


def test_average_exception2(self):
    with self.assertRaises(ValueError):
        average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()
