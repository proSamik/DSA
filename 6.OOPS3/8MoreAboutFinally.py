#More about Finally

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
        value = num/denom

    except ValueError:
        print("Numerator and Denominator should be integers")

    except ZeroDenomiatorError:
        print("ZeroDenominator Error is raised")

    except ZeroDivisionError:
        print("Division by zero is not allowed")
    
    except: 
        print("Some exception is raised")
    
    else:
        print(value)
        break

    finally:
        # print(num)
        # print(denom)
        # print(value)
        print("Exception may or may not be raised")
    
    