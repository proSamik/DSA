class MapNode:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    #Counstructor
    def __init__(self):
        self.bucketSize = 10
        self.buckets = [None]*10
        self.count = 0

    #returns size
    def size(self):
        return self.count

    #compression function which returns index
    def getBucketIndex(self,hc):
        return abs((hc))%self.bucketSize

    #insert element in map
    def insert(self,key,value):
        hc = hash(key) #hash function
        index = self.getBucketIndex(hc)
        head = self.buckets[index]

        while head != None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        
        head = self.buckets[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count+=1
    
    #get value of given key
    def getValue(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]

        while head != None:
            if head.key == key:
                return head.value
            head = head.next
        
        return None
    
    #remove the node of the given key
    def remove(self,key):
        hc = hash(key)
        index = self.getBucketIndex(hc)
        head = self.buckets[index]
        prev = None

        while head != None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -=1
                return head.value
            prev = head
            head = head.next
        
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