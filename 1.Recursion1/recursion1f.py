#Check if list sorted

def isSorted(a):
    l= len(a)
    if l==0 or l==1:
        return True
    elif a[0]>a[1]:
        return False
    smallerList = a[1:]

    isSmallerSorted = isSorted(smallerList)

    return isSmallerSorted


list1= [1,2,3,5,7,9]
print(isSorted(list1))

list2= [1,5,7,3,9]
print(isSorted(list2))