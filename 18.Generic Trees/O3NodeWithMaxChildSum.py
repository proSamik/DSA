from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.sum = 0


def maxSumNode(tree):
    if tree is None:
        return tree, 0
    
    if len(tree.children) == 0:
        tree.sum = tree.data
        return tree

    maxNode = tree
    maxSum = tree.data
    maxChildNode = tree
    maxChildSum = tree.data
    for child in tree.children:
        maxSum += child.data
        tempMaxNode= maxSumNode(child)
        if tempMaxNode.sum > maxChildSum:
            maxChildSum = tempMaxNode.sum
            maxChildNode = tempMaxNode

    tree.sum = maxSum
    if maxChildNode.sum > tree.sum:
        maxNode = maxChildNode
    
    return maxNode


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
tree = createLevelWiseTree(arr)
temp= maxSumNode(tree)
print(temp.data)