from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def lengthLL(head):
    cnt=0
    while head.next!=None:
        cnt+=1
        head=head.next
    return cnt
    


def bubbleSort(head):
    if head is None:
        return head
        
    n=lengthLL(head)
    for i in range(n):
        prev = None
        curr=head
        for j in range(0,n-i):
            nextNode = curr.next
            if curr.data>nextNode.data:
                if prev is None:
                    curr.next=nextNode.next
                    nextNode.next=curr
                    head=nextNode
                else:
                    prev.next=curr.next
                    curr.next=nextNode.next
                    nextNode.next=curr
            # printLinkedList(head)
                prev=nextNode
            else:
                prev=curr
                curr=curr.next

    return head



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
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)