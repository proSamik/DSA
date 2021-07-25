# print 1 to n
def print1toN(n):
    if n==0:
        return 
    print1toN(n-1)
    print(n)

def printNto1(n):
    if n==0:
        return 
    print(n)
    printNto1(n-1) 

n= int(input())

printNto1(n)