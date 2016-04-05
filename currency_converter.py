class CurrencyConverter:

    def __init__(self, exchange_rate={'USD': 1, 'EUR': 0.88}):
        self.exchange_rate = exchange_rate

    def default_exchange_rates(self):
        self.exchange_rate = {'USD': 1.0,
                            'EUR' : 0.87774
                            'GBP' : 0.70077
                            'INR' : 66.1158
                            'AUD' : 1.31447
                            'CAD' : 1.30651}


    def convert(self, from_currency, to_code):
        if (to_code not in exchange_rate.keys() or
            from_currency.code not in exchange_rate.keys()):
            raise UnknownCurrencyCodeError("Currency is missing. Cannot convert.")
        elif from_currency.code == to_code:
            to_currency = from_currency
            return to_currency
        else:
            to_currency = Currency(to_code,
                            (from_currency.value *
                            self.exchange_rate[to_code] /
                            self.exchange_rate[from_code]))
            return to_currency


class UnknownCurrencyCodeError(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
