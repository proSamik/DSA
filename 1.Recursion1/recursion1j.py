#1. Last Index of number using recursion without copying

#2.Last Index of number copying list 


def lastIndex(a, si, x):
    l= len(a)

    if si==l:
        return -1
    
    inDex = lastIndex(a,si+1,x)

    if inDex == -1:
        if a[si]==x:
            return si

    return inDex

def lastIndexs(a,x):
    l= len(a)

    if l==0:
        return -1
    
    smallerList = a[1:]

    smallOutput = lastIndexs(smallerList,x)

    if smallOutput!=-1:
        return 1 + smallOutput

    if smallOutput == -1:
        if a[0] == x:
            return 0
    
    return smallOutput 
    

a= [1,2,3,4,6,1,6,8,9,0,5,1,7,8,9]

print(a)
x= int(input())
print(lastIndex(a,0,x))
print(lastIndexs(a,x))