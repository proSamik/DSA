from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAndOddHead(head):
    even=odd=None
    evenTemp=oddTemp=None

    while head!= None:
        data = head.data
        newNode = Node(data)
        
        if data%2!=0:
            if odd is None:
                odd=newNode
                oddTemp=newNode
            else:
                oddTemp.next = newNode
                oddTemp = oddTemp.next
        elif data%2==0:
            if even is None:
                even=newNode
                evenTemp=newNode
            else:
                evenTemp.next = newNode
                evenTemp = evenTemp.next
        head = head.next
    return odd, even




def evenAfterOdd(head) :
    
    odd, even = evenAndOddHead(head)

    if odd== None:
        return even

    curr = odd
    while curr.next!= None:
        curr=curr.next
    

    curr.next = even

    return odd

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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1