#Erros and exception

#ERRORS

#Syntax errors
#ZeroDivisionError
#NameError
#TypeError
#valueError - passing a string instead of int

#Intro to Exception Handling


#how to except error and handle the exception

#try and except method

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

    # except NameError:

    #     print("This is name error")


    #Below will handle any error if we are not specific
    except :
        print("Numerator and Denominator should be integers")

