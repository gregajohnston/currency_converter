import unittest
from currency import Currency


class TestCurrency(unittest.TestCase):

    def test_assign_value_one_arg(self):
        self.assertEqual(Currency('$5.5').value, 5.5)

    def test_assign_code_one_arg(self):
        self.assertEqual(Currency('$5.5').code, "USD")

    def test_assign_value_two_arg(self):
        self.assertEqual(Currency('EUR', 10).value, 10)

    def test_assign_code_two_arg(self):
        self.assertEqual(Currency('EUR', 10).code, "EUR")

    def test_is_equal(self):
        self.assertTrue(Currency() == Currency('$1'))

    def test_is_not_equal(self):
        self.assertFalse(Currency() != Currency('$1'))

    def test_assert_equal(self):
        self.assertEqual(Currency('$1') + Currency('$1'), Currency('$2'))

    def test_assert_equal(self):
        self.assertEqual(Currency('$10') - Currency('$8'), Currency('$2'))

    def test_assert_equal(self):
        self.assertEqual(Currency('$10') * 2, Currency('$20'))

if __name__ == '__main__':
    unittest.main()
