#Pair sum in array

from sys import stdin

def pairSum(arr, n, num) :
	
    m = [0] * 10000

    for i in range(n):
        m[arr[i]]+=1
    
    cnt =0 

    for i in range(n):
        cnt += m[num-arr[i]]
    
        if num - arr[i]==arr[i]:
            cnt-=1
    
    return cnt//2

#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1