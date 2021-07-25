#Check if list sorted without copying list

def isSorted(a):
    l= len(a)
    if l==0 or l==1:
        return True
    elif a[0]>a[1]:
        return False

    a.remove(a[0])

    isSmallerSorted = isSorted(a)

    return isSmallerSorted


list1= [1,2,3,5,7,9]
print(isSorted(list1))

list2= [1,5,7,3,9]
print(isSorted(list2))

list3= [1,3,9,10,100,500,501,507,509]
print(isSorted(list3))