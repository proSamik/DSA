from sys import stdin
from sys import maxsize as MAX_VALUE
     
def countMinStepsToOneI(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    # print(dp[1], dp[2], dp[3])
    i = 4
    while i <= n:
        ans1 = ans2 = ans3 = MAX_VALUE

        if i%3 == 0:
            ans3 = dp[i//3]

        if i%2 == 0:
            ans2 = dp[i//2]
            # print(i, "ans2", ans2)
        
        ans1 = dp[i-1]

        dp[i] = 1 + min(ans1, ans2, ans3)
        # print(i,dp[i])
        
        i += 1

    return dp[n]

#main
n = int(stdin.readline().rstrip())
ans = countMinStepsToOneI(n)
print(ans)