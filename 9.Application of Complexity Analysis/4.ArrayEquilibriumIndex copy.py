#Array Equilibirium Index
from sys import stdin

def arrayEquilibriumIndex(arr, n) :

    if n<=2:
        return -1
        
    left = 0
    right = 0
    for i in range(n):
        right+=arr[i]
    
    key =-1
    right -= arr[0]
    for i in range(1,n):
        left += arr[i-1]
        right -= arr[i]
        # print(arr[:i],'      ', arr[i+1:])

        # print(f"left={left}  right= {right}")
        if left == right:
            key =i
            break
    
    return key


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