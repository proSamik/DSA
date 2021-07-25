from sys import stdin


#merge
def merge(a,a1,a2):
    
    i=j=k=0

    while i<len(a1) and j <len(a2):
        if a1[i]<a2[j]:
            a[k]= a1[i]
            i+=1
            k+=1
        elif a1[i]>a2[j]:
            a[k] =  a2[j]
            j+=1
            k+=1
        elif a1[i]==a2[j]:
            a[k]= a1[i]
            i+=1
            k+=1

            a[k] =  a2[j]
            j+=1
            k+=1

    
    while i <len(a1):
        a[k]= a1[i]
        i+=1
        k+=1
    
    while j <len(a2):
        a[k]= a2[j]
        j+=1
        k+=1



#merge Sort
def mergeSort(a):
    
    n = len(a)

    if n==0:
        return a

    if n==1:
        return a[0]
    
    mid = n//2

    a1 = (a[:mid])
    a2= a[mid:]

    mergeSort(a1)
    mergeSort(a2)

    merge(a,a1,a2)

def findUnique(arr, n) :


    if n==0:
        return arr
        
    if n==1:
        return arr[0]
    
    mergeSort(arr)

    if arr[0]!=arr[1]:
        return arr[0]

    elif arr[n-1]!=arr[n-2]:
        return arr[n-1]
    
    else:
        i=1
        while i<=n-2:
            if arr[i]!=arr[i-1] and arr[i]!=arr[i+1]:
                return arr[i]
            i+=1

    return -1

    

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
    print(findUnique(arr, n))

    t-= 1

# a= [2, 3, 1, 6, 3, 6, 2]

# print(findUnique(a,7))