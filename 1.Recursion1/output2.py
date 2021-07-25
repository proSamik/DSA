def checkNumber(arr, x):
    n = len(arr)

    if(n==0):
        return False

    elif(arr[0]==x):
         return True

    arr.remove(arr[0])

    return checkNumber(arr,x) 

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())

if checkNumber(arr, x):
    print('true')
else:
    print('false')
