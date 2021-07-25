#Insert At ith position- iteratively CN

class Node:

    def __init__(self,data):
        self.data= data
        self.next= None

def insertionLL(head,i,num):

    if i<0 or i>lengthLL(head):
        return head

    cnt = 0
    prev = None
    curr = head
    
    while cnt < i:
        prev =curr
        curr = curr.next
        cnt+=1

    newNode = Node(num)

    if prev is not None:
        prev.next = newNode
    else:    
        head = newNode
    newNode.next = curr

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
