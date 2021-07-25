#Except Functionality

class ZeroDenomiatorError(ZeroDivisionError):
    pass

while True:
    try:
        n = input('Enter the numerator: ')
        num = int(n)
        n = input('Enter the Denominator: ')
        denom = int(n)
        if denom == 0:
            raise ZeroDenomiatorError("Denominator should not be zero")
            #order will be followed line by line
        value = num/denom
        print(value)
        break

    except ValueError:
        print("Numerator and Denominator should be integers")

    #order will be followed line by line
    except ZeroDenomiatorError:
        print("ZeroDenominator Error is raised")

    except ZeroDivisionError:
        print("Division by zero is not allowed")
    
    except: 
        print("Some exception is raised")
    
    