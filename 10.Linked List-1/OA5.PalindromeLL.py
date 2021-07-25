
from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def reverseLL(head):

    if head.next is None:
        return head
    
    revHead= reverseLL(head.next)

    tail = revHead

    while tail.next is not None:
        tail = tail.next
    
    tail.next = head
    head.next = None

    return revHead

def clone(head):
    newHead = None
    tail= None
    i=0
    while head is not None:
        newNode = Node(head.data)
        if newHead is None:
           newHead = newNode
           tail = newNode
        else:
            tail.next= newNode
            tail = newNode
        head = head.next
        i+=1

    return newHead 


def isPalindrome(head) :

    if head is None:
        return True
        
    newHead = clone(head)
    revHead= reverseLL(head)

    # printLinkedList(newHead)
    # printLinkedList(revHead)

    while newHead is not None and revHead is not None:
        if newHead.data != revHead.data:
            return False
        newHead =  newHead.next
        revHead= revHead.next
    
    return True

def lengthLL(head):
    cnt = 0
    while head is not None:
        cnt+=1
        head = head.next
    
    return cnt

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
    
    if isPalindrome(head) :
        print('true')
    else :
        print('false')
        
    t -= 1