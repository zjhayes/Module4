import unittest

from store.coupon_calculations import calculate_price


class MyTestCase(unittest.TestCase):

    def test_price_under_ten(self):
        price = calculate_price(9, 3, 10)
        self.assertEquals(5.95, price)


if __name__ == '__main__':
    unittest.main()
