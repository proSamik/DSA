# Handling Multiple Exceptions

while True:
    try:
        n = input('Enter the numerator: ')
        num = int(n)
        n = input('Enter the Denominator: ')
        denom = int(n)
        value = num/denom
        print(value)
        break

    # except ValueError:
    #     print("Numerator and Denominator should be integers")
    
    # except ZeroDivisionError:
    #     print("Denominator should be not zero")

    #if we want to handle two errors we have to specify

    #except (ValueError, ZeroDivisionError):

    except (ValueError, ZeroDivisionError):
        print("Numerator and Denominator should be integers and Denominator should not be zero")
