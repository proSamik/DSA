#Longest Increasing subsequence

#######################
#######################
#######   MY    #######
#######  CODE   #######
######################
######################


from sys import stdin
def lis(arr): 
    
    n = len(arr)

    if n == 1:
        return 1

    longest = float("-inf")

    for i in range(n):
        tempLong = float("-inf")

        for j in range(i+1,n):
            if arr[j] > arr[i]:
                ans = lis(arr[j:])
                tempLong = max(ans,tempLong)
            elif j == n-1:
                tempLong = max(0,tempLong)

        longest = max(tempLong,longest)
    
    return  1 + longest




def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
print(lis(arr))