#Push, pop, top, size, isempty,
#it should be O(1) for push and pop


from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :

    #Define data members and __init__()
    def __init__(self):
        self.__cnt=0
        self.__head= None

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
       return self.__cnt

    def isEmpty(self) :
        return self.__cnt==0

    def push(self, data) :
        #Implement the push(element) function
        newNode= Node(data)
        newNode.next=self.__head
        self.__head=newNode
        self.__cnt+=1

    def pop(self) :
        #Implement the pop() function
        if self.isEmpty()!=True:
            popEle=self.__head.data
            self.__head=self.__head.next
            self.__cnt-=1
            return popEle
        else:
            return -1
        

    def top(self) :
        #Implement the top() function
        if self.isEmpty()!=True:
            return self.__head.data
        else:
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