def firstIndex(si, arr, x):
    l = len(arr)
     
    if si==l:
        return -1
    if arr[si] == x:
        return si
    inDex = firstIndex(si+1, arr, x)

    return inDex
     

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(0, arr, x))