from sys import stdin
import sys
import heapq as heap

class LinkedListNode :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class Queue :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.size = 0
        
    def enqueue(self, data) :
        newNode = LinkedListNode(data)
        if self.head is None :
            self.head = self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return
        
    def dequeue(self) :
        if self.head is None :
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def getSize(self) :
        return self.size
    
    def isEmpty(self) :
        if self.head is None :
            return True
        return False
    
    def peek(self) :
        if self.head is None :
            return None
        return self.head.data
    
def buyTicket(arr, n, k) : 
    q = Queue()

    for i in range(n):
        q.enqueue(arr[i])

    heap._heapify_max(arr)

    count = 0   #timer

    while True:
        if arr[0] == q.peek() and k == 0:
            count += 1
            return count

        elif arr[0] == q.peek():
            count += 1
            # print(arr, q.peek())
            # print()
            heap._heappop_max(arr)
            q.dequeue()
            k -= 1
        
        else:
            ele = q.dequeue()
            q.enqueue(ele)
            if k == 0:
                k = q.getSize()-1
            else:
                k -= 1


#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return n, list(), int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(stdin.readline().strip())
    return n, arr, k

#main
sys.setrecursionlimit(10**6)
n, arr, k = takeInput()
print(buyTicket(arr, n, k))