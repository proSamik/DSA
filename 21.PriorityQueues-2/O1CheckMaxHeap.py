def checkMaxHeap(lst,i=0):
    n = len(lst)
    if n<=1 :
        return True
    
    parentIndex = i
    leftCI = 2 * parentIndex + 1
    rightCI = 2* parentIndex + 2
    leftCIResult = rightCIResult = True
    if leftCI < n:
        temp = lst[parentIndex] > lst[leftCI]
        result = checkMaxHeap(lst,leftCI)
        leftCIResult = temp and result
    
    if rightCI < n:
        temp =  lst[parentIndex] > lst[rightCI]
        result = checkMaxHeap(lst,rightCI)
        rightCIResult = temp and result
    
    return leftCIResult and rightCIResult

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')