import heapq

li = [1,5,8,7,4,9,11]

#Build heap
heapq.heapify(li)
print(li)

#Heap add element
heapq.heappush(li,2)
print(li)

#Heap remove element
print(heapq.heappop(li))
print(li)

#replace the min
print(heapq.heapreplace(li,6))
print(li)

