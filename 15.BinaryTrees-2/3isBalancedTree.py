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

def isBalanced(root):
    if root is None:
        return True
    
    leftHeight = nodeHeight(root.left)
    rightHeight = nodeHeight(root.right)
    diff = abs(leftHeight-rightHeight)

    if diff>1:
        return False

    left_isBalanced = isBalanced(root.left)
    right_isBalanced =  isBalanced(root.right)

    return left_isBalanced and right_isBalanced

root = treeInput()
printTreeDetailed(root)
print(isBalanced(root))