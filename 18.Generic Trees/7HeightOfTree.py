from sys import stdin,setrecursionlimit

#main
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def treeHeight(root):
    if root is None:
        return 0
    maxHeight = 0
    for child in root.children:
        maxHeight = max(maxHeight,treeHeight(child))
    return 1 + maxHeight
    
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
arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
tree = createLevelWiseTree(arr)
height = treeHeight(tree)
print(height)