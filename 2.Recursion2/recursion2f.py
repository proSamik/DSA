#Quick Sort my code

#Problem, timed out

def partition(a,si,ei):

    cnt=0
    key=a[si]
    for k in range(si,ei+1):
        if key>a[k]:
            cnt+=1
    
    p = si+cnt

    a[si],a[p]= a[p],a[si]

    i=si
    j=ei

    while(i < p and j>p):
        # This if take times, it should be in else

        # if (a[i] > a[p]) and (a[j]<a[p]):
        #     a[i],a[j] = a[j],a[i]
        #     i+=1
        #     j-=1
    
        if(a[i]<a[p]):
            i+=1

        elif(a[j]>a[p]):
            j-=1

        else:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1

    return p



def quickSort(a,si,ei):

    if si>=ei:
        return 
    
    i = partition(a,si,ei)

    quickSort(a, si, i-1)
    quickSort(a,i+1,ei)

# a= [11,128,24,5,0,1,4,2,256,14]

# quickSort(a,0, len(a)-1)

# print(a)

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr,end=' ')