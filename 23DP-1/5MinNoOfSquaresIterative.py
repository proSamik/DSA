import sys 
sys.setrecursionlimit(10**6)

def minStepsTo1(n,dp):
    if n == 0:
        return 0

    ans = sys.maxsize

    i = 1
    while i*i <= n:
        if dp[n - i*i] == -1:
            tempAns = minStepsTo1(n - i*i,dp)
            dp[n - i*i] = tempAns
        else:
            tempAns = dp[n - i*i]

        ans = min(ans, tempAns)
        i += 1
    
    return 1 + ans

def minStepsTo1I(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        j = 1
        ans = sys.maxsize
        while j*j <= i:
            tempAns = dp[i - j*j]
            ans = min(ans, tempAns)
            j += 1
        # print(i,j, end= ' ')
        dp[i] = 1 + ans

    return dp[n]
           
n = int(input())
ans = minStepsTo1I(n)
print(ans)





