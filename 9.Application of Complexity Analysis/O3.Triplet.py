#Pair sum in array

from sys import stdin

def tripletSum(arr, n, num) :

    if n<3:
        return 0

    arr.sort()

    cnt=0

    for i in range(n-2):
        l=i+1
        r=n-1
    
        while l<r:
            target =arr[i] + arr[l] +arr[r]
            if num==target:
                cnt+=1
                while arr[l]==arr[l+1]:
                    cnt+=1
                    l+=1

                while arr[r]==arr[r-1]:
                    cnt+=1
                    r-=1

                l+=1
                r-=1
            elif num>target:
                l+=1
            elif num<target:
                r-=1

    return cnt



#taking input using fast I/O method
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
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1