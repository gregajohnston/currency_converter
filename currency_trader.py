from currency import Currency
from currency_converter import CurrencyConverter


class CurrencyTrader:

    def __init__(self, converter_old, converter_new, starting_currency):
        self.converter_old = converter_old
        self.converter_new = converter_new
        self.starting_currency = starting_currency

    def maximize_investment(self):
        exchange = 0
        best_code = ""
        for key in self.converter_old:
            if self.converter_old[key]/self.converter_new[key] > exchange:
                exchange = self.converter_old[key]/self.converter_new[key]
                best_code = key

        intermediate_currency = self.converter_old(self.starting_currency, best_code)
        final_currency = self.converter_new(intermediate_currency, self.starting_currency.code)

        return final_currency
