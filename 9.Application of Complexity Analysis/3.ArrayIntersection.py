#Array Intersection Binary search

from sys import stdin

def merge(a1,a2,a):
    i=0
    j=0
    k=0

    while i<len(a1) and j<len(a2):
        if(a1[i]<a2[j]):
            a[k]= a1[i]
            k+=1
            i+=1
        
        elif a1[i]>a2[j]:
            a[k]=a2[j]
            k+=1
            j+=1
        
        elif a1[i]== a2[j]:
            a[k]= a1[i]
            k+=1
            i+=1

            a[k]=a2[j]
            k+=1
            j+=1
    
    while i<len(a1):
        a[k]= a1[i]
        k+=1
        i+=1

    while j<len(a2):
        a[k]=a2[j]
        k+=1
        j+=1

def mergeSort(a):

    if len(a)==0 or len(a)==1:
        return a
        
    mid = len(a)//2

    a1=a[0:mid]
    a2=a[mid:]

    mergeSort(a1)
    mergeSort(a2)

    merge(a1,a2,a)

def intersection(arr1, arr2, n, m) :
    
    if n == 0 or m ==0:
        return 

    
    if n<m:
        mergeSort(arr1)

        for i in range(m):
            a= arr2[i]
            si= 0
            ei = n
            key = -1
            while si<=ei:
                mid = (si+ei)//2

                if a == arr1[mid]:
                     key = mid
                     break
                elif a<arr1[mid]:
                    ei =mid-1
                else:
                    si = mid +1
            if key!=-1:
                print(arr1[key], end = ' ')

    else:
        mergeSort(arr2)

        for i in range(n):
            a= arr1[i]
            si= 0
            ei = m
            key = -1
            while si<=ei:
                mid = (si+ei)//2

                if a == arr2[mid]:
                     key = mid
                     break
                elif a<arr1[mid]:
                    ei =mid-1
                else:
                    si = mid +1
            if key!=-1:
                print(arr2[key], end = ' ')
    




# Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
    	return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    intersection(arr1, arr2, n, m)
    print()

    t -= 1