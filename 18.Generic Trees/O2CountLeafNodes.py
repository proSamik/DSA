import sys
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(root):
    if root is None:
        return True, 0
    isLeaf = False
    leafCount = 0

    if len(root.children)==0:
        isLeaf = True
    
    for child in root.children:
        isSmallLeaf, isSmallCount = leafNodeCount(child)
        if isSmallLeaf:
            leafCount += 1
        else:
            leafCount += isSmallCount
    
    if isLeaf:
        return isLeaf, 1 + leafCount

    return isLeaf, leafCount

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
isLeaf, leafNodes = leafNodeCount(tree)
print(leafNodes)