from sys import stdin

def longestConsecutiveSubsequence(arr,n):
    d = {}
    index = {}
    if n==0:
        return []
    j = 0
    for i in arr:
        d[i] = True
        index[i] = j
        j += 1
    
    # print(d)
    start = 0
    end = 0
    maxLength = 0
    l = list()

    for k in arr:
        tempCount = 0
        i = k + 1
        while (i in d) and (d[i] != False):
            tempCount += 1
            d[i] = False
            i += 1
        
        i = k-1 
        while (i in d) and (d[i] != False):
            tempCount += 1
            d[i] = False
            i-=1
        
        if tempCount >= maxLength and tempCount>0:
    
            if maxLength > 0 and tempCount == maxLength:
                indexOfPrevStart = index[start]
                # print(f"index of start is {indexOfPrevStart} ")
                indexOfNowStart = index[i+1]
                # print(f"index of nowStart is {indexOfNowStart}")
                if indexOfPrevStart > indexOfNowStart :
                    start = i+1
                    maxLength = tempCount

            if maxLength == 0 or tempCount>maxLength:
                start = i+1
                maxLength = tempCount
                 
            end = start + maxLength

    l.append(start)
    l.append(end)
    
    return l

def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n
    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)