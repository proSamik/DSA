#Insert At ith position- iteratively

class Node:

    def __init__(self,data):
        self.data= data
        self.next= None

def insertionLL(head,i,num):
    cnt = 0
    newNode = Node(num)
    curr = head
    
    while cnt <= lengthLL(head):
        if i==0 and cnt == i:
            head = newNode
            newNode.next = curr
            return head
        elif cnt == i:
            prev.next = newNode
            newNode.next= curr
            return head
        else:
            prev = curr
            curr = curr.next
            cnt+=1

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
