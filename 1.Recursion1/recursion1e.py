#Change maximum depth of python

import sys
sys.setrecursionlimit(3000)

def factorial(n):

    if n==0:
        return 1
    return n* factorial(n-1)


n=int(input())

print(factorial(n))