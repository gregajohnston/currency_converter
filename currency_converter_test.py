import unittest
from currency_converter import CurrencyConverter
from currency import Currency


class TestCurrencyConverter(unittest.TestCase):

    def test_assign_value_no_arg(self):
        self.assertEqual(CurrencyConverter().exchange_rate, {'USD': 1, 'EUR': 0.88})

    def test_assign_code_one_arg(self):
        self.assertEqual(CurrencyConverter({'USD': 1, 'EUR': 0.88, 'GBP': 0.7}).exchange_rate, {'USD': 1, 'EUR': 0.88, 'GBP': 0.7})

    def test_convert(self):
        self.assertEqual(CurrencyConverter().convert(Currency(), 'EUR'), Currency('EUR', 0.88))



if __name__ == '__main__':
    unittest.main()
