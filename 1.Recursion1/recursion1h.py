#Check if list sorted without copying and without removing the elements of list

def isSortedBetter(a, si):
    l= len(a)
    
    if si == l-1 or si ==l:
        return True
    if a[si] > a[si +1]:
        return False
    isSmallerPartSorted = isSortedBetter(a, si+1)

    return isSmallerPartSorted

list1= [1,2,3,5,7,9]
print(isSortedBetter(list1,0))

list2= [1,5,7,3,9]
print(isSortedBetter(list2,0))