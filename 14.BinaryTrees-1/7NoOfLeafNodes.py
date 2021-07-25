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

def numleafNodes(root):
    if root is None:
        return 0
    
    if root.left==None and root.right==None:
        return 1

    leftLeafNodes = numleafNodes(root.left)
    rightLeafNodes = numleafNodes(root.right)
    totalLeafNodes = leftLeafNodes + rightLeafNodes
    return totalLeafNodes
    

root = treeInput()
printTreeDetailed(root)

print(numleafNodes(root))