#Array Equilibirium Index
from sys import stdin

def arrayEquilibriumIndex(arr, n) :

    if n<=2:
        return -1
        
    left = 0
    right = 0
    total=0
    for i in range(n):
        total+=arr[i]
    
    left= 0
    i=0
    while i< len(arr):
        right= total - left - arr[i]
        if left == right:
            return i
        
        left += arr[i]
        i+=1

    return -1
    
    
#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t-= 1