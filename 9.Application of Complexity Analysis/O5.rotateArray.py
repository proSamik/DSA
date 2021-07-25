from sys import stdin


def rotate(arr, n, d):
    d= d%n
    if d==0:
        return
    else:
        a1= a[:d]
        a2=a[d:]
        
        for i in range(n-d):
            arr[i]=a2[i]
        
        i=0
        for j in range(n-d,n):
            arr[j]=a1[i]
            i+=1

#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1