#Else and Finally

#If no exception has been made in try block then only the else block will work.

#if we have try > except > finally 

#OR

# try > except >else >finally

#Finally will be executed every time

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

    except ValueError:
        print("Numerator and Denominator should be integers")

    #order will be followed line by line
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
        print("Exception may or may not be raised")
    
    