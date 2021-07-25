class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTree(root):
    # Not a Base case, this is an edge case
    if root is None:
        return

    print(root.data,end =':')
    for child in root.children:
        printTree(child)

def printTreeDetailed(root):
    if root is None:
        return
    
    print(root.data,end=' : ')
    for child in root.children:
        print(child.data,end=', ')
    
    print()
    for child in root.children:
        printTreeDetailed(child)

n1 = TreeNode(5)
n2 = TreeNode(2)
n3 = TreeNode(9)
n4 = TreeNode(8)
n5 = TreeNode(7)
n6 = TreeNode(15)
n7 = TreeNode(1)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)

printTree(n1)
print()
printTreeDetailed(n1)

#    5
#2   9   8   7
#  15 1