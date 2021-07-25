from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def merge(head1, head2):

    newHead= None
    tail= None

    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
            if newHead is None:
               newHead = head1
               tail = head1
            else:
                tail.next = head1
                tail = tail.next
            # print(tail.data,end=' ')
            head1= head1.next

        elif head2.data<=head1.data:
            if newHead is None:
               newHead = head2
               tail = head2
            else:
                tail.next = head2
                tail = tail.next
            # print(tail.data,end=' ')
            head2= head2.next
            
    
    while head1 is not None:
        if newHead is None:
               newHead = head1
               tail = head1
        else:
            tail.next = head1
            tail = tail.next
        # print(tail.data,end=' ')
        head1= head1.next
     
    while head2 is not None:
        if newHead is None:
               newHead = head2
               tail = head2
        else:
            tail.next = head2
            tail = tail.next
        # print(tail.data,end=' ')
        head2= head2.next
    
    return newHead

def midHead(head):
    slow = fast = head

    while fast.next is not None and fast.next.next is not None:
        slow= slow.next
        fast= fast.next.next
    
    return slow

def mergeSort(head):

    if head is None or head.next is None:
        return head

    mid = midHead(head)

    head1= head
    head2= mid.next
    mid.next = None

    newHead1 = mergeSort(head1)
    newHead2 = mergeSort(head2)

    newHead = merge(newHead1, newHead2)

    return newHead

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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1


# Sample Input 1 :
# 1
# 10 9 8 7 6 5 4 3 -1
# Sample Output 1 :
#  3 4 5 6 7 8 9 10 
#  Sample Output 2 :
# 2
# -1
# 10 -5 9 90 5 67 1 89 -1
# Sample Output 2 :
# -5 1 5 9 10 67 89 90 