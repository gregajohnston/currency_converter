from currency import Currency
from currency_converter import CurrencyConverter


class CurrencyTrader:

    def __init__(self, converter_old=CurrencyConverter(), converter_new=CurrencyConverter(), starting_currency=Currency()):
        self.converter_old = converter_old
        self.converter_new = converter_new
        self.starting_currency = starting_currency

    def maximize_value(self):
        exchange = 0
        best_code = ""
        for key in self.converter_old.exchange_rate:
            if self.converter_old.exchange_rate[key]/self.converter_new.exchange_rate[key] > exchange:
                exchange = self.converter_old.exchange_rate[key]/self.converter_new.exchange_rate[key]
                best_code = key
        intermediate_currency = self.converter_old.convert(self.starting_currency, best_code)
        final_currency = self.converter_new.convert(intermediate_currency, self.starting_currency.code)
        return final_currency
