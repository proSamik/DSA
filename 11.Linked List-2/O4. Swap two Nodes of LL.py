from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
    posi=posj=0
    curr= head
    swapValueA= swapValueB= None
    prevA=prevB=None
    while posi<i and curr!= None:
        prevA=curr
        curr=curr.next
        posi+=1
    swapValueA= curr
    
    curr=head
    while posj<j and curr!=None:
        prevB=curr
        curr=curr.next
        posj+=1
    swapValueB= curr
    
    if prevA!=None:
        prevA.next=swapValueB
    else:
        head=swapValueB
    if prevB!=None:
        prevB.next=swapValueA

    temp = swapValueA.next
    swapValueA.next = swapValueB.next
    swapValueB.next=temp

    return head
      

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1