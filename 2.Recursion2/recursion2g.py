#Quick sort cn
def partition(a,si,ei):

    pivot =a[si]

    #Find no. of elements smaller than pivot

    c=0

    for i in range(si,ei+1):
        if a[i]<pivot:
            c+=1
    
    a[si+c],a[si]=a[si],a[si+c]

    pivotIndex = si + c

    i= si
    j=ei

    while i<j:
        if (a[i]<pivot):
            i+=1
        elif a[j] >= pivot:
            j-=1
        else:
            a[i],a[j] =a[j],a[i]
            i+=1
            j-=1
    
    return pivotIndex


def quickSort(a, si, ei):
    if si>=ei:
        return
    pivotIndex = partition(a,si,ei)

    quickSort(a, si, pivotIndex-1)
    quickSort(a,pivotIndex+1,ei)

a= [10,9,7,1,3,5,4,2]

quickSort(a,0, len(a)-1)

print(a)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr,end=' ')