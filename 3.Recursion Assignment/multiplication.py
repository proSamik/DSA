#Multiplication Using recursion

def multiplyRec(m,n):

    if m== 0 or n ==0:
        return 0
    if n<0:
        return -(m + multiplyRec(m,(abs(n)-1)))
    return (m + multiplyRec(m,n-1))



from sys import setrecursionlimit

setrecursionlimit(100000)


m=int(input())
n=int(input())

print(multiplyRec(m,n))
