import unittest

from store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        price = calculate_price(9, 5, 10)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 5, 15)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 5, 20)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 10, 10)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 10, 15)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 10, 20)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 15, 10)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 15, 15)
        self.assertEquals(5.95, price)

    def test_price_under_ten(self):
        price = calculate_price(9, 15, 20)
        self.assertEquals(5.95, price)

if __name__ == '__main__':
    unittest.main()
