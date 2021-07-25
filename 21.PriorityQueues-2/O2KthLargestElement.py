import heapq
def kthLargest(lst, k):
    n = len(lst)
    minHeap = lst[:k]
    heapq.heapify(minHeap)

    for i in range(k,n):
        if lst[i] > minHeap[0]:
            heapq.heapreplace(minHeap,lst[i])
    
    return minHeap[0]


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)