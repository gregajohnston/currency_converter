import unittest
from currency_trader import CurrencyTrader
from currency_converter import CurrencyConverter
from currency import Currency


class TestCurrencyConverter(unittest.TestCase):

    def test_assign_value_no_converter(self):
        self.assertEqual(CurrencyTrader().converter_old.exchange_rate, {'USD': 1, 'EUR': 0.88})

    def test_assign_value_no_currency(self):
        self.assertEqual(CurrencyTrader().starting_currency.code, 'USD')

    def test_maximize_value_return_value(self):
        self.assertEqual(CurrencyTrader(
                            CurrencyConverter({'USD': 1, 'EUR': 2, 'GBP': 2, 'JPY': 7.5}),
                            CurrencyConverter({'USD': 1, 'EUR': 1, 'GBP': 2.1, 'JPY': 5}),
                            Currency('$10')).maximize_value().value, 20.0)

    def test_maximize_value_return_code(self):
        self.assertEqual(CurrencyTrader(
                            CurrencyConverter({'USD': 1, 'EUR': 2, 'GBP': 2, 'JPY': 7.5}),
                            CurrencyConverter({'USD': 1, 'EUR': 1, 'GBP': 2.1, 'JPY': 5}),
                            Currency('$10')).maximize_value().code, 'USD')


if __name__ == '__main__':
    unittest.main()
