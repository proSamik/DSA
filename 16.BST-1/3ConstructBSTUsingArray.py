import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst,si,ei):
    size = len(lst)
    if si>ei:
        return None

    mid = si + (ei-si)//2

    rootData = lst[mid]
    root = BinaryTreeNode(rootData)
    
    leftSubTree = constructBST(lst,si,mid-1)
    
    rightSubTree = constructBST(lst,mid+1,ei)

    root.left = leftSubTree
    root.right = rightSubTree

    return root
    

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst,0,n-1)
preOrder(root)