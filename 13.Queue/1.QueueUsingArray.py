
class Queue:

    def __init__(self):
        self.__q=[]
        self.__front=0
        self.__cnt=0
    
    def enqueue(self,data):
        self.__q.append(data)
        self.__cnt+=1
    
    def dequeue(self):
        if self.__cnt>0:
            item=self.__q[self.__front]
            self.__front+=1
            self.__cnt-=1
            return item
        return -1

    def front(self):
        if self.__cnt>0:
            return self.__q[self.__front]
        return -1

    def size(self):
        return self.__cnt

    def isEmpty(self):
        return self.__cnt==0


q1= Queue()
q1.enqueue(10)
q1.enqueue(29)

print(q1.front())
print(q1.dequeue())
print(q1.size())
print(q1.dequeue())
print(q1.isEmpty())