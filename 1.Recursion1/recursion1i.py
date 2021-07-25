# First index of a number with copying

def firstIndex(arr, x):
    l = len(arr)

    if l == 0:
        return -1
    if arr[0] == x:
        return 0
    
    smallerArr = arr[1:]

    smallOutput = firstIndex(smallerArr,x)

    if smallOutput==-1:
        return -1
        
    index = 1 + smallOutput
    return index


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))