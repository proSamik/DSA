from sys import stdin
from sys import setrecursionlimit
from sys import maxsize as MAX_VALUE

setrecursionlimit(10**6)

def countMinStepsToOne(n,dp) :
    if n == 1:
        return 0

    myAns1 = myAns2 = myAns3 = MAX_VALUE

    if dp[n-1] == -1:
        myAns1 = countMinStepsToOne(n-1,dp)
        dp[n-1] = myAns1
    else:
        myAns1 = dp[n-1]

    if n%2 == 0:
        if dp[n//2] == -1:
            myAns2 = countMinStepsToOne(n//2,dp)
            dp[n//2] = myAns2
        else:
            myAns2 = dp[n//2]
    
    if n%3 == 0:
        if dp[n//3] == -1:
            myAns3 = countMinStepsToOne(n//3,dp)
            dp[n//3] = myAns3
        else:
            myAns3 = dp[n//3]
    
    print(n, 1 + min(myAns1,myAns2,myAns3))
    return 1 + min(myAns1,myAns2,myAns3)
     



#main
n = int(stdin.readline().rstrip())
dp = [-1] * n
print(countMinStepsToOne(n,dp))