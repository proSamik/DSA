#Duplicate In Array
from sys import stdin

def findDuplicate(arr, n) :

    count = [1] * n
    i=0
    while i<n:
        if count[arr[i]] == 2:
            return arr[i]
        else:
            count[arr[i]]+=1
        i+=1

#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1