#Append Last N To First
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def lenLL(head):
    cnt=0
    while head is not None:
        cnt+=1
        head = head.next
    
    return cnt

def appendLastNToFirst(head, n) :
    
    cnt =0
    curr= head

    l = lenLL(head)
    if n<=0 or n>=l:
        return head

    while cnt < l-n-1:
        curr = curr.next
        cnt+=1
    
    temp = head
    head = curr.next
    curr.next = None

    curr = head

    while curr.next is not None:
        curr = curr.next
    
    curr.next = temp

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
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 