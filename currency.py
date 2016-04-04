class Currency:

    def __init__(self, *args="$1.00"):
        if len(args) == 1:
            self.code = args[0][0]
            self.value = args[0][1:]
        elif len(args) == 2:
            self.code = args[0]
            self.value = args[1]
        else:
            raise TypeError

    def is_equal(self, other):
        return self.code == other.code and self.value == other.value

    def add(self, other):
        try:
            if self.code != other.code:
                raise DifferentCurrencyCodeError
        except DifferentCurrencyCodeError:
            print("Cannot add different currencies.")
        return self.value + other.value

    def subtract(self, other):
        try:
            if self.code != other.code:
                raise DifferentCurrencyCodeError
        except DifferentCurrencyCodeError:
            print("Cannot add different currencies.")
        return self.value - other.value

    def multiply(self, multiple):
        return self.value * multiple
