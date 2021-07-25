def downHeapify(arr,i,n):
    parentIndex = i
    leftChildIndex =  2*parentIndex + 1
    rightChildIndex = 2*parentIndex + 2

    while leftChildIndex < n:
        minIndex = parentIndex
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
        if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex
        
        if minIndex == parentIndex:
            break
        arr[parentIndex], arr[minIndex] = arr[minIndex], arr[parentIndex]
        parentIndex = minIndex
        leftChildIndex =  2*parentIndex + 1
        rightChildIndex = 2*parentIndex + 2


def heapSort(arr):
    #Build the heap
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        downHeapify(arr,i,n)

    #Remove n elements from heap and put them at correct position
    for i in range(n-1, 0 , -1):
        arr[0], arr[i], = arr[i], arr[0]
        downHeapify(arr,0,i)
    
n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=' ')