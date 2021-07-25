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

def isBST2(root):
    if root is None:
        return float("+inf"),float("-inf"), True
    
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isrightBST = isBST2(root.right)

    minimum= min(leftMin, rightMin,root.data)
    maximum = max(leftMax,rightMax, root.data)

    isTreeBST = root.data>leftMax and root.data<=rightMin and isLeftBST and isrightBST
    return minimum, maximum, isTreeBST
    
# Main
root = takeLevelWiseTreeInput()
printTreeDetailed(root)
maxNode= float("-inf")
minNode = float("+inf")
print(isBST2(root))