from sys import stdin

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def mergeTwoSortedLinkedLists(head1, head2):

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


# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head1 = takeInput()
    head2 = takeInput()

    newHead = mergeTwoSortedLinkedLists(head1, head2)
    printLinkedList(newHead)

    t -= 1

# 1
# 2 5 8 12 -1
# 3 6 9 -1

#2 3 5 6 8 9 12 

# Sample Input 2 :
# 2
# 2 5 8 12 -1
# 3 6 9 -1
# 10 40 60 60 80 -1
# 10 20 30 40 50 60 90 100 -1
# Sample Output 2 :
# 2 3 5 6 8 9 12 
# 10 10 20 30 40 40 50 60 60 60 80 90 100