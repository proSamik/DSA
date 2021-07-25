#Experimental analysis

#MERGE SORT CN
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


#Selection Sort
def selectionSort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]

def revArr(n):
    l1=[]
    for i in range(n,0,-1):
        l1.append(i)
    return l1

#main
import time

n=100000
a= revArr(n)

#merge Sort
start = time.time()
mergeSort(a)
end = time.time()
print(n, end-start)

n=100000
a= revArr(n)

#selection Sort
start = time.time()
selectionSort(a)
end = time.time()
print(n, end-start)