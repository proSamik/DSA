#Pair sum in array

from sys import stdin

def factorial(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    
    return fact

def tripletSum(arr, n, num) :
    arr.sort()
    cnt=0
    
    if n==1 or n==0:
        return 0
    
    key = arr[0]
    duplicate = True
    for i in range(1,n):
        if key!=arr[i]:
            duplicate = False
            break

    if duplicate==True and 3*arr[0]==num:
        cnt = int(factorial(n)//(factorial(n-3)*6))
        return cnt
    
    
    cnt=0
    i=0
    while i< n-1:
        l=i+1
        r=n-1
        x=arr[l]
        y=arr[r]
        z=arr[i]
        k = num-z 
        while l<r: 
            x=arr[l]
            y=arr[r]      
            p=x+y
            if p<k:#Case 1

                l=l+1
            elif p>k:#case 2

                r=r-1
            else:#Case 3

                cnt+=1

                while l+1<r and arr[l+1]==x:
                    
                    l+=1

                    cnt+=1

                while r-1>l and arr[r-1]==y:
                    r-=1

                    cnt+=1

                l+=1
                r-=1

        i+=1

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