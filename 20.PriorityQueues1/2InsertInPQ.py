#min Priority Queue

class PriorityQueueNode:
    def __init__(self,value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize()==0

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
    
    def __percolateUp(self):
        childIndex = self.getSize()-1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,value,priority):
        pqNode = PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
    
    def removeMin(self):
        pass