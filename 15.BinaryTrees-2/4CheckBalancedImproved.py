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

def nodeHeight(root):
    if root is None:
        return 0
    leftHeight = nodeHeight(root.left)
    rightHeight = nodeHeight(root.right)

    return 1 + max(leftHeight,rightHeight)

def getHeightAndCheckBalance(root):
    if root is None:
        return 0, True
    
    lh,left_isBalanced = getHeightAndCheckBalance(root.left)
    rh, right_isBalanced = getHeightAndCheckBalance(root.right)

    h = 1+ max(lh,rh)
    checkBalance= abs(lh-rh)<2 and left_isBalanced and right_isBalanced
    return h, checkBalance

root = treeInput()
printTreeDetailed(root)

def isBalanced2(root):
    h, isRootBalanced = getHeightAndCheckBalance(root)
    return isRootBalanced
print(isBalanced2(root))