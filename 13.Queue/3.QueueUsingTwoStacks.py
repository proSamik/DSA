#Implementing queue using 2 stacks

#either enque or dequeue can be O(n)

#Stack class
class Stack:

    def __init__(self):
        self.__data=[]
    
    def push(self,item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        else:    
            return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return -1
        return self.__data[len(self.__data)-1]
    
    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size()==0

#Queue using two stacks
class QueueUsingTwoStacks:

    def __init__(self):
        self.__inputStack=Stack()
        self.__emptyStack=Stack()
        self.__cnt=0
    
    def enqueue(self,data):
        if self.__cnt>0:
            while(self.__inputStack.size()!=0):
                self.__emptyStack.push(self.__inputStack.pop())
            
            self.__inputStack.push(data)

            while(self.__emptyStack.size()!=0):
                self.__inputStack.push(self.__emptyStack.pop())
        else:
            self.__inputStack.push(data)
        
        self.__cnt+=1
    
    def dequeue(self):
        if self.__cnt>0:
            item=self.__inputStack.pop()
            self.__cnt-=1
            return item
        else:
            return -1
    
    def front(self):
        if self.__cnt>0:
            return self.__inputStack.top()
        return -1
    
    def isEmpty(self):
        return self.__cnt==0

q= QueueUsingTwoStacks()

q.enqueue(10)
q.enqueue(20)
q.enqueue(35)
q.enqueue(50)

while not q.isEmpty():
    print(q.dequeue())