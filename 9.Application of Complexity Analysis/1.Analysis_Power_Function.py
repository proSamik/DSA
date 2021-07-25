# Power with optimal time complexity

def pow(x,n):

    if n==0:
        return 1
    smallPow = pow(x,n//2)

    if n%2== 0:
        return smallPow*smallPow
    else:
        return x * smallPow *smallPow

print(pow(3,4))