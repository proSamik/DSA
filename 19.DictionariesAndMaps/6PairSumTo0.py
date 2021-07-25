from sys import stdin

#This will not run for all numbers are 0
def pairSum0Approach1(l,n):
    d = {}
    count = 0
    for i in l:
        d[i] = d.get(i,0) + 1
    
    for i in l:
        if -i in d:
            temp1 = d[-i]
            temp2 = d[i]
            d[-i] = 0
            d[i] = 0
            count += (temp1 + temp2)
    
    return count


def pairSum0Approach2(l,n):
    d = {}
    count = 0 
    for i in l:
        if -i in d:
            temp = d[-i]
            count += temp
            
        d[i] = d.get(i,0) + 1
    
    return count

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))