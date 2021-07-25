from sys import stdin

def lis(arr,i,n,dp):

    if i == n:
        return 0, 0

    including_max = 1

    for j in range(i+1,n):
        if arr[j] > arr[i]:
            if dp[j] == -1:
                ans = lis(arr,j,n,dp)
                dp[j] = ans
                further_including_max = ans[0]
            else:
                further_including_max = dp[j][0]
            including_max = max(including_max, 1 + further_including_max)
    
    if dp[i+1] == -1:
        ans = lis(arr,i+1,n,dp)
        dp[i+1] = ans
        excluding_max = ans[1]
    else:
        excluding_max = dp[i+1][1]

    overallMax = max(including_max, excluding_max)

    return including_max, overallMax

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    

arr,n=takeInput()
dp = [-1] * (n+1)
print(lis(arr,0,n,dp)[1])