import queue
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

#Input of Binary Tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root is None:
        return
    print(root.data,end=':')

    if root.left!=None:
        print('L',root.left.data,end=',',sep='')
    
    if root.right!=None:
        print('R',root.right.data,end=' ',sep='')
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def treeInput():
    rootData= int(input())
    if rootData == -1:
        return None

    root= BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left= leftTree
    root.right= rightTree
    return root

def printLL(head):
    while head is not None:
        print(str(head.data),'->',end=' ')
        head = head.next   
    print()

def levelWiseLL(root):
    q1 = queue.Queue()
    q2 = queue.Queue()
    q1.put(root)
    heads = list()

    while not q1.empty():
        head = None
        tail = None
        while not q1.empty():
            curr = q1.get()
            newNode = Node(curr.data)
            if head is None:
                head = newNode
            else:
                temp.next = newNode
            temp = newNode

            if curr.left!=None:
                q2.put(curr.left)
            if curr.right!=None:
                q2.put(curr.right)

        q1,q2 = q2,q1
        heads.append(head)

    return heads         

root = treeInput()
printTreeDetailed(root)
print()
heads = levelWiseLL(root)

for head in heads:
    printLL(head)