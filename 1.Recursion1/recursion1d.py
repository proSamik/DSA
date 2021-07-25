#Fibonacci using recursion

def fib(n):
    if n==1 or n==2:
        return 1
    Output = fib(n-1) + fib(n-2)
    
    return Output

n= int(input())

print(fib(n))