import Math

class Currency:

    def __init__(self, *args):
        if len(args) == 0:
            self.code = "USD"
            self.value = 1.0
        elif len(args) == 1:
            self.code = args[0][0:1]
            self.value = args[0][1:]
        elif len(args) == 2:
            self.code = args[0]
            self.value = args[1]
        else:
            raise TypeError("Must import 0, 1 or 2 arguments")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.code == other.code:
                return self.value + other.value
            else:
                raise DifferentCurrencyCodeError("Cannot add different currencies")
        raise ValueError("Both variables not type Currency")

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.code == other.code:
                return self.value - other.value
            else:
                raise DifferentCurrencyCodeError("Cannot add different currencies")
        raise ValueError("Both variables not type Currency")

    def __mul__(self, number):
        if type(number) == int or type(number) == float:
            self.value = self.value * other.value
            return self
        else:
            raise ValueError("Must multiple by a int or float")
        raise ValueError("Requires two arguments, a currency and an int (or float)")
