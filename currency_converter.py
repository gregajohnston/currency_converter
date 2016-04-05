from currency import Currency


class CurrencyConverter:

    def __init__(self, exchange_rate={'USD': 1, 'EUR': 0.88}):
        self.exchange_rate = exchange_rate

    def has_unknown_codes(self, to_code, from_code):
        return (to_code not in self.exchange_rate or
            from_code not in self.exchange_rate)

    def create_rate(self, from_currency, to_code):
        return self.exchange_rate[to_code] / self.exchange_rate[from_currency.code]

    def convert(self, from_currency, to_code):
        if from_currency.code == to_code:
             return from_currency
        elif self.has_unknown_codes(to_code, from_currency.code):
            raise UnknownCurrencyCodeError("Currency is missing. Cannot convert.")
        else:
            return Currency(to_code, from_currency.value * self.create_rate(from_currency, to_code))

    #{'USD': 1.0,
    #'EUR' : 0.87774,
    #'GBP' : 0.70077,
    #'INR' : 66.1158,
    #'AUD' : 1.31447,
    #'CAD' : 1.30651}

class UnknownCurrencyCodeError(Exception):
    pass
