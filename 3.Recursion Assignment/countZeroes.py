#Count Zeroes in given integer

def countZero(n):

    if n/10==0:
        return 0
    
    smallOutput= countZero(n//10)

    if n%10==0:
        return 1 + smallOutput
    else:
        return smallOutput

from sys import setrecursionlimit

setrecursionlimit(3000)

n= int(input())

print(countZero(n))