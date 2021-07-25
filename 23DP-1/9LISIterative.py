from sys import stdin

def lisI(arr,n):

    #This is important
    dp = [[0 for j in range(2)] for i in range(n+1)] 

    for i in range(n-1,-1,-1):
        includingMax = 1
        print(arr[i], end =" ")
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                print('\t', arr[j], end= ' ')
                includingMax = max(includingMax, 1 + dp[j][0])
                print(dp)

        print()
        dp[i][0] = includingMax
        excludingMax = dp[i+1][1]
        overallMax = max(includingMax, excludingMax)  
        dp[i][1] = overallMax

    print(dp)
    return dp[0][1]      

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n


arr,n=takeInput()
print(lisI(arr,n))