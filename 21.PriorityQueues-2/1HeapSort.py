def downHeapify(arr,i,n):
    parentIndex = i
    leftChildIndex = 2*parentIndex + 1
    rightChildIndex = 2*parentIndex + 2
    while leftChildIndex < n :
        minIndex = parentIndex
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
        if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex
        
        if parentIndex == minIndex:
            break

        arr[minIndex], arr[parentIndex] = arr[parentIndex], arr[minIndex]
        parentIndex = minIndex
        leftChildIndex = 2*parentIndex + 1
        rightChildIndex = 2*parentIndex + 2

def buildHeap(arr):
    n = len(arr)
    nonLeaf = (n//2) - 1
    for i in range(nonLeaf,-1,-1):
        downHeapify(arr,i,n)
        
def heapSort(arr):
    buildHeap(arr)
    # print("After building heap", arr)
    n = len(arr)
    for i in range(0,n):
        # print(arr)
        arr[0], arr[n-1-i] = arr[n-1-i], arr[0]
        # print("afterSwap=",arr)
        size = n-1-i
        downHeapify(arr,0,size)

    

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')