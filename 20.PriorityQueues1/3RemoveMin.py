class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
        
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def __percolateDown(self):
        parentIndex = 0
        childIndex1 = 2 * parentIndex + 1
        childIndex2 = 2 * parentIndex + 2
        while childIndex2 < self.getSize():
            if self.pq[childIndex1].priority < self.pq[childIndex2].priority:
                if self.pq[parentIndex].priority > self.pq[childIndex1].priority:
                    self.pq[parentIndex], self.pq[childIndex1] = self.pq[childIndex1], self.pq[parentIndex]
                    parentIndex = childIndex1
            else:
                if self.pq[parentIndex].priority > self.pq[childIndex2].priority:
                    self.pq[parentIndex], self.pq[childIndex2] = self.pq[childIndex2], self.pq[parentIndex]
                    parentIndex = childIndex2

            childIndex1 = 2 * parentIndex + 1
            childIndex2 = 2 * parentIndex + 2


    def removeMin(self):
        if self.isEmpty():
            return None
        elem = self.pq[0].ele
        self.pq[0] = self.pq.pop()
        self.__percolateDown()
        return elem
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    