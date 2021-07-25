import heapq

li = [1,5,4,7,8,9,2,3]

#Build max heap
heapq._heapify_max(li)
print(li)

#pop at top
print(heapq._heappop_max(li))
print(li)

#push element
li.append(6)
heapq._siftdown_max(li,0,len(li)-1)
print(li)


#replace with max
print(heapq._heapreplace_max(li,0))
print(li)
