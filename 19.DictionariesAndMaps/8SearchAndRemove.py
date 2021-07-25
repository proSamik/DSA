class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value= value
        self.next = None

class Map:
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None]* 10
        self.count = 0

    def size(self):
        return self.count
    
    def getBucketIndex(self,hc):
        return (abs(hc)%(self.bucketSize))

    def insert(self,key,value):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]

        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        
        head = self.buckets[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1
    
    def getValue(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]

        while head is not None:
            if key == head.key:
                return head.value
            head = head.next
        
        return None
    
    def remove(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = tail = self.buckets[index]
        prev= None

        while tail is not None:
            if tail.key == key:
                if prev is None:
                    self.buckets[index] = tail.next
                else:
                    prev.next = tail.next
                self.count -= 1
                return tail.value
            prev = tail
            tail = tail.next
        return None


m = Map()
m.insert('Parikh',2)
print(m.getValue('Parikh'))
print(m.size())
m.insert('Rohan',7)
print(m.size())
m.insert('Parikh',9)
print(m.size())
print(m.getValue('Parikh'))
print(m.getValue('Samik'))
print(m.remove('Rohan'))
print(m.size())
print(m.remove('Samik'))
print(m.size())