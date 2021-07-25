#Custom Exception

#raise is used before the exception name to call it

#it will just throw that exception

#let's create custom exception

class ZeroDenomiatorError(Exception):
    pass

while True:
    try:
        n = input('Enter the numerator: ')
        num = int(n)
        n = input('Enter the Denominator: ')
        denom = int(n)
        if denom == 0:
            raise ZeroDenomiatorError("Denominator should not be zero")
        print('Hi')
        value = num/denom
        print(value)
        break

    except ValueError:
        print("Numerator and Denominator should be integers")

    except ZeroDivisionError:
        print("Division by zero is nor allowed")
    
    except ZeroDenomiatorError:
        print("ZeroDenominator Error is raised")