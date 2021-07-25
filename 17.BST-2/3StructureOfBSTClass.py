class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    #Print tree helper
    def printTreeHelper(self, root):
        if root is None:
            return
        print(root.data,end=':')

        if root.left!=None:
            print('L',root.left.data,end=', ',sep='')
        
        if root.right!=None:
            print('R',root.right.data,end=' ',sep='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    #this will print the tree
    def printTree(self):
        return self.printTreeHelper(self.root)
    
    def isPresentHelper(self,root,data):
        if root is None:
            return False
        
        if root.data == data:
            return True
        
        if root.data > data:
            #Call on left
            return self.isPresentHelper(root.left,data)
        else:
            #Call on right
            return self.isPresentHelper(root.right,data)

    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)
    
    def insertHelper(self,root,data):
        if root is None:
            node = BinaryTreeNode(data)
            return node
        
        if data < root.data:
            leftNode = self.insertHelper(root.left,data)
            root.left = leftNode

        elif data >= root.data:
            rightNode = self.insertHelper(root.right,data)
            root.right = rightNode
        
        return root

    def insert(self,data):
        self.root = self.insertHelper(self.root,data)
        self.numNodes+=1

    def minNode(self,root):
        if root is None:
            return float("+inf")
        
        if root.left is None:
            return root.data

        return self.minNode(root.left)

    def deleteDataHelper(self,root,data):
        if root is None:
            return False, root
        
        if root.data< data:
            deleted, newRightNode = self.deleteDataHelper(root.right,data)
            root.right = newRightNode
            return deleted, root
        
        if root.data > data:
            deleted, newLefttNode = self.deleteDataHelper(root.left, data)
            root.left = newLefttNode
            return deleted, root
        
        #root is leaf
        if root.left is None and root.right is None:
            return True, None

        #root has one child
        if root.left is None:
            return True, root.right
        
        if root.right is None:
            return True, root.left

        #root has two children
        replacement = self.minNode(root.right)
        root.data = replacement
        deleted, newRightNode =  self.deleteDataHelper(root.right,replacement)
        root.right = newRightNode
        return deleted, root

    def deleteData(self, data):
        deleted, newRoot = self.deleteDataHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root = newRoot
        return deleted

    def count(self):
        return self.numNodes


b = BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTree()
print(b.count())
print(b.isPresent(10))
print(b.isPresent(7))
print(b.deleteData(4))
print(b.deleteData(10))

b.printTree()