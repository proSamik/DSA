#Insert at ith position recursively

class Node:

    def __init__(self,data):
        self.data= data
        self.next= None

def insertionLL(head,i,data):
    
    if i<0:
        return head

    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    
    if head is None:
        return None
    
    smallHead = insertionLL(head.next,i-1,data)
    head.next = smallHead
    
    return head
    

def lengthLL(head):
    l = 0
    while head is not None:
        l+=1
        head= head.next
    return l

def printLL(head):
    while head is not None:
        print(str(head.data),'->',end=' ')
        head= head.next
    
    print(head)

def takeInput():
    
    inputList = [int(x) for x in input().split()]

    head = None
    tail = None

    for currData in inputList:

        if currData == -1:
            break

        newNode = Node(currData)

        if head is None:
            head= newNode
            tail= newNode
        
        else:
            tail.next= newNode
            tail = newNode
    
    return head
    
head=takeInput()

printLL(head)

head = insertionLL(head,3,9)
head = insertionLL(head,0,8)
head = insertionLL(head,lengthLL(head),7)
printLL(head)
