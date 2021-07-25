class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTreeDetailed(root):
    if root is None:
        return
    
    print(root.data,end=' : ')
    for child in root.children:
        print(child.data,end=', ')
    
    print()
    for child in root.children:
        printTreeDetailed(child)

def takeTreeInput():
    print("Enter root Data")
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = TreeNode(rootData)

    childrenCount  = int(input(f"Enter number of children for {rootData}: "))

    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    
    return root

root = takeTreeInput()
print()
printTreeDetailed(root)

#    5
#2   9   8   7
#  15 1