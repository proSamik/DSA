from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    if tree is None:
        return None
    
    minNode = None

    if tree.data>n:
        minNode = tree
    
    for child in tree.children:
        minDataNode = nextLargest(child,n)
        if minDataNode!=None:
            if minNode is None and minDataNode.data>n:
                minNode = minDataNode
            elif minDataNode.data>n and minDataNode.data<minNode.data:
                minNode = minDataNode

    
    return minNode
    





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
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n).data)