#Length of LL (recursive)

from sys import stdin , setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Taking Input Using Fast I/O
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


# To print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()

def lengthRecursive(head):
    
    if head is None:
        return 0
    
    smallOutput =lengthRecursive(head.next)

    return 1 + smallOutput

    pass



# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    head = takeInput()
    ans=lengthRecursive(head)
    print(ans)
    t -= 1 