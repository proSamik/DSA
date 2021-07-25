#Lowest Common Ancestor
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

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

#LCA of BST
def lcaOfBST(root,n1,n2):
    if root is None or root.data==n1 or root.data==n2:
        return root
    
    if root.data>n1 and root.data>n2:
        return lcaOfBST(root.left,n1,n2)
    elif root.data<n1 and root.data<n2:
        return lcaOfBST(root.right,n1,n2)
    else:
        lcaOfLeft = lcaOfBST(root.left,n1,n2)
        lcaOfright = lcaOfBST(root.right, n1, n2)
        if lcaOfLeft != None and lcaOfright!=None:
            return root
        if lcaOfLeft!=None:
            return lcaOfLeft
        if lcaOfright!=None:
            return lcaOfright
    
# Main
root = takeLevelWiseTreeInput()
printTreeDetailed(root)
print()
n1 = int(input())
n2 = int(input())
lcaRoot = lcaOfBST(root,n1,n2)
if lcaRoot!=None:
    print(lcaRoot.data)

