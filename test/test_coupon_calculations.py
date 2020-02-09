import unittest

from store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        price = calculate_price(9, 5, 10)
        self.assertEquals(9.77, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 5, 15)
        self.assertEquals(9.55, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 5, 20)
        self.assertEquals(9.34, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 10, 10)
        self.assertEquals(5.0, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 10, 15)
        self.assertEquals(5.05, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 10, 20)
        self.assertEquals(5.1, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 15, 10)
        self.assertEquals(0.23, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 15, 15)
        self.assertEquals(0.54, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 15, 20)
        self.assertEquals(0.86, price)

if __name__ == '__main__':
    unittest.main()
