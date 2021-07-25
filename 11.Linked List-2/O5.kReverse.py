from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

#Reverse the LL
def reverse(head):
    newHead= None
    curr=head
    prev= None

    while curr!=None:
        newNode= curr.next
        curr.next= prev
        prev= curr
        curr= newNode
    
    newHead= prev
    return newHead

def kReverse(head, k) :
	
    #Base
    if head is None or head.next is None or k==0:
        return head
    
    #IH
    curr=temp=head
    i=0
    while curr!=None and i<k:
        temp=curr
        curr=curr.next
        i+=1
    
    newKhead= kReverse(curr,k)

    #IS
    if temp!=None:
        temp.next= None
    revHead= reverse(head)
    head.next= newKhead

    return revHead


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
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1