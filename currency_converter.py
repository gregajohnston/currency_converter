class CurrencyConverter:
    def __init__(self, rate_dict={'USD': 1, 'EUR': 0.88}):
        self.rate_dict = rate_dict

    def convert(self, currency, code):
        if code == currency.code:
            return_currency = currency
            return return_currency
        if code != currency.code:
            return_currency = Currency(code, currency.value)
            return return_currency * rate_dict[code]


    # rate_dict={'USD': 1.00,
    #         'EUR' : 0.87774
    #         'GBP' : 0.70077
    #         'INR' : 66.1158
    #         'AUD' : 1.31447
    #         'CAD' : 1.30651}
