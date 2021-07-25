#Sum of n digits

def sumOfDigits(s):
    
    if s/10==0:
        return 0
    
    smalloutput = sumOfDigits(s//10)

    val = s%10 + smalloutput
    return val

from sys import setrecursionlimit

setrecursionlimit(3000)

s= int(input())

print(sumOfDigits(s))