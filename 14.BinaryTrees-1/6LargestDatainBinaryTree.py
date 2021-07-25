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

def largestData(root):
    if root is None:
        return -1  #ideally return -infinity
    
    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)
    largest = max(root.data, leftLargest, rightLargest)
    return largest
    

root = treeInput()
printTreeDetailed(root)
print(largestData(root))