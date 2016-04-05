# Currency

This class contains data for currency objects. Each currency object holds a currency code (string of 3 letters denoting the country) and a value (for storing an amount of currency). Objects may be created with 0, 1 or 2 arguments as follows:

Currency() creates an instance with the default value of a currency code ('USD') and a value (1).
Currency('¥12') creates an instance with code 'JPY' and value 12. Note that calling the class in this way will convert currency symbols to their respective currency codes.
Currency('EUR', 5.5) creates an instance with code 'EUR' and value 5.5.

The Currency class overrides several basic methods, allowing for equality and non-equality operations as well as special addition, subtraction and multiplication.

# CurrencyConverter

This class contains an object that interacts with the currency class. The converter can be called without an argument for the default dictionary {'USD': 1, 'EUR': 0.88}, or can be called with a dictionary as an argument.

The dictionary provided must have currency codes as keys and their exchange rates (relative to the US dollar) as the values.

CurrencyConverter includes one method, convert, that can take a provided currency object and a different currency code and, using exchange rates, return a new currency object that has a value converted into the new currency.
