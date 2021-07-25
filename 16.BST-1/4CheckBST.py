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
        print("Enter left child of", currentNode.data)
        leftChildData= int(input())
        if leftChildData!=-1:
            leftChild = BinaryTreeNode(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)
        
        print("Enter right child of", currentNode.data)
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

def minTree(root):
    if root is None:
        return float("+inf")
    
    leftMinima = minTree(root.left)
    rightMinima = minTree(root.right)

    return min(leftMinima,rightMinima,root.data)

def maxTree(root):
    if root is None:
        return float("-inf")
    
    leftMaxima = maxTree(root.left)
    rightMaxima = maxTree(root.right)

    return max(leftMaxima,rightMaxima,root.data)

def isBST(root):
    if root is None:
        return True
    
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)

    if root.data>rightMin or root.data<=leftMax:
        return False
    
    isLeftBST = isBST(root.left)
    isrightBST = isBST(root.right)

    return isrightBST and isLeftBST
    
# Main
root = takeLevelWiseTreeInput()
printTreeDetailed(root)
maxNode= float("-inf")
minNode = float("+inf")
print(isBST(root))