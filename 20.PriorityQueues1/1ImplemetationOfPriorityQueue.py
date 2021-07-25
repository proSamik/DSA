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
    
    def insert(self,value,priority):
        pass
    
    def removeMin(self):
        pass