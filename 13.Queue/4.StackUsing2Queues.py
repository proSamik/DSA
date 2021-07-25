
from sys import stdin

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

class Stack :
    #Define data members and __init__()
    def __init__(self):
        self.__inputQueue=Queue()
        self.__emptyQueue=Queue()
        self.__cnt=0

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.__cnt



    def isEmpty(self) :
        #Implement the isEmpty() function
        return self.__cnt==0



    def push(self, data) :
        #Implement the push(element) function
        if self.__cnt>0:
            while self.__inputQueue.size()!=0:
                self.__emptyQueue.enqueue(self.__inputQueue.dequeue())
            
            self.__inputQueue.enqueue(data)

            while self.__emptyQueue.size()!=0:
                self.__inputQueue.enqueue(self.__emptyQueue.dequeue())
        
        else:
            self.__inputQueue.enqueue(data)

        self.__cnt+=1


    def pop(self) :
        #Implement the pop() function
        if self.__cnt>0:
            item = self.__inputQueue.dequeue()
            self.__cnt-=1
            return item
        return -1

    def top(self) :
        #Implement the top() function
        if self.__cnt>0:
            return self.__inputQueue.front()
        return -1
		

#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1