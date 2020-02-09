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

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 5, 10)
        self.assertEquals(17.49, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 5, 15)
        self.assertEquals(16.96, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 5, 20)
        self.assertEquals(16.43, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 10, 10)
        self.assertEquals(12.72, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 10, 15)
        self.assertEquals(12.46, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 10, 20)
        self.assertEquals(12.19, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 15, 10)
        self.assertEquals(7.95, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 15, 15)
        self.assertEquals(7.95, price)

    def test_price_under_between_ten_thirty(self):
        price = calculate_price(15, 15, 20)
        self.assertEquals(7.95, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 5, 10)
        self.assertEquals(17.49, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 5, 15)
        self.assertEquals(16.96, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 5, 20)
        self.assertEquals(16.43, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 10, 10)
        self.assertEquals(12.72, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 10, 15)
        self.assertEquals(12.46, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 10, 20)
        self.assertEquals(12.19, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 15, 10)
        self.assertEquals(7.95, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 15, 15)
        self.assertEquals(7.95, price)

    def test_price_under_between_thirty_fifty(self):
        price = calculate_price(25, 15, 20)
        self.assertEquals(7.95, price)


if __name__ == '__main__':
    unittest.main()
