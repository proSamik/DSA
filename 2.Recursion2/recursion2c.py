# Binary Search Using recursion

def binarySearch(a,x,si,ei):

    l= len(a)

    if si>ei:
        return -1
    
    mi = (si+ei)//2

    if a[mi]==x:
        return mi

    elif a[mi]> x:
        ei= mi-1

        return binarySearch(a,x,si,ei)

    elif a[mi] < x:
        si = mi+1

        return binarySearch(a,x,si,ei)

    


l1= [1,2,5,7,8,9,22,25,26,29,35]

l = len(l1)-1
print(l1)
x = int(input())

print(binarySearch(l1,x,0,l))
