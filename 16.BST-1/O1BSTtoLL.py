from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data),'->', end = ' ')
        head = head.next
    print(head)

#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Taking level-order input using fast I/O method
def takeLevelWiseTreeInput():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())

    if rootData ==-1:
        return None
    
    root= BinaryTreeNode(rootData)
    q.put(root)

    while not q.empty():
        currentNode = q.get()
        # print("Enter left child of", currentNode.data)
        leftChildData= int(input())
        if leftChildData!=-1:
            leftChild = BinaryTreeNode(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)
        
        # print("Enter right child of", currentNode.data)
        rightChildData= int(input())
        if rightChildData!=-1:
            rightChild = BinaryTreeNode(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)
    return root
    
def printTreeDetailed(root):
    if root is None:
        return
    print(root.data,end=':')

    if root.left!=None:
        print('L',root.left.data,end=', ',sep='')
    
    if root.right!=None:
        print('R',root.right.data,end=' ',sep='')
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

#Converting BST into Sorted Linked List
def convertBSTtoLL(root):
    if root is None:
        return None, None
    
    newNode = Node(root.data)

    leftHead, leftTail = convertBSTtoLL(root.left)

    if leftHead is None:
        head = newNode
    else:
        head = leftHead

    if head.next is None:
        head.next = newNode
    if leftTail!=None:
        leftTail.next = newNode
    leftTail = newNode

    rightHead, rightTail = convertBSTtoLL(root.right)

    leftTail.next = rightHead

    if rightHead is None:
        return head, leftTail
    
    return head, rightTail

    
# Main
root = takeLevelWiseTreeInput()
printTreeDetailed(root)
print()

head, tail =  convertBSTtoLL(root)
printLL(head)
print()
