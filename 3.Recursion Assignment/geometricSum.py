#1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 


def geometricSum(k):

    if k==0:
        return 1
    
    smallOutput=float( geometricSum(k-1))

    ans = 1/(2**k) 

    return float( ans + smallOutput )

k= int(input())

ans = geometricSum(k) 

print("{0:.5f}".format(ans))


