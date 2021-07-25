from sys import stdin
def maxfreq(arr):

    maxFreq = -1
    maxElem = 0
    dictNum = {}

    for num in arr:
        dictNum[num] = dictNum.get(num,0) + 1
        maxFreq = max(maxFreq, dictNum[num])
    
    for i in arr:
        if dictNum[i] == maxFreq:
            maxElem = i
            break
    
    return maxElem

 
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))