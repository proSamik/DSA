from sys import stdin,setrecursionlimit
import queue
#main
setrecursionlimit(10**6)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printTreeDetailed(root):
    if root is None:
        return
    
    print(root.data,end=' : ')
    for child in root.children:
        print(child.data,end=', ')
    
    print()
    for child in root.children:
        printTreeDetailed(child)

def takeTreeInputLevelWise():
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None
    
    root = TreeNode(rootData)
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        numchildren = int(input(f"Enter no. of children  {currentNode.data}: "))
        for i in range(numchildren):
            childData = int(input(f"Enter next child for {currentNode.data}: "))
            child = TreeNode(childData)
            currentNode.children.append(child)
            q.put(child)
    
    return root


root = takeTreeInputLevelWise()
print()
printTreeDetailed(root)
print()