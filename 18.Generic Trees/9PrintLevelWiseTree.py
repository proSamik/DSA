import sys, queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def printLevelWiseTree(root):
    if root is None:
        return
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currNode = q.get()
        print(currNode.data,end=":")
        size = len(currNode.children)
        childCount = 0
        for i in range(size):
            child = currNode.children[i]
            print(child.data,end='')
            if childCount<size-1:
                print(end=',')
            childCount+=1
            q.put(child)
        print()

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)