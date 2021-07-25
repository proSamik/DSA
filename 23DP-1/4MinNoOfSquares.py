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

           
n = int(input())
dp = [-1] * (n+1)
ans = minStepsTo1(n,dp)
print(ans)





