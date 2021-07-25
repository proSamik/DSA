import heapq
def kSmallest(lst, k):
    smallList = lst[:k]
    heapq._heapify_max(smallList)

    for i in range(k,len(lst)):
        if smallList[0] > lst[i]:
            heapq._heapreplace_max(smallList, lst[i])
    
    return smallList


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')