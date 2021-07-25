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

a=[10,5,3,1,7,9,4]

print(mergeSort(a))

print(a)
