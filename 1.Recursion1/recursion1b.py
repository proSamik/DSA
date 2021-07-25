#Sum of first natural numbers

def sumOfN(n):

    if(n==0):
        return 0
    smallOutput = sumOfN(n-1)
    output = n + smallOutput
    return output


n = int(input())

print(sumOfN(n))