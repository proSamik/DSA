#Self coded BST Class

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    #For Inserting
    def insertHelper(self,root,data):
        if root is None:
            return BinaryTreeNode(data)
        
        if root.data <= data:
            rightRoot = self.insertHelper(root.right,data)
            root.right = rightRoot
            return root
        
        if root.data > data:
            leftRoot = self.insertHelper(root.left,data)
            root.left = leftRoot
            return root

    def insert(self,data):
        self.root = self.insertHelper(self.root,data)
        self.numNodes+=1

    #For Deleting
    def minNode(self,root):
        if root is None:
            return
        
        if root.left is None:
            return root.data
        
        return self.minNode(root.left)

    def deleteHelper(self,root,data):
        if root is None:
            return False, None

        if root.data< data:
            deleted, rightNode = self.deleteHelper(root.right,data)
            root.right = rightNode
            return deleted, rightNode
        
        elif root.data>data:
            deleted, leftNode = self.deleteHelper(root.left,data)
            root.left = leftNode
            return deleted, root
        
        #For No child
        if root.left is None and root.right is None:
            return True, None
        
        #For One child
        if root.left is None:
            return True, root.right
        if root.right is None:
            return True, root.left
        
        #For Two children
        replacement = self.minNode(root.right)
        root.data = replacement
        deleted, rightNode = self.deleteHelper(root.right,replacement)
        root.right = rightNode
        return deleted, root

    def delete(self,data):
        deleted, self.root = self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        return deleted

    #For Searching
    def searchHelper(self,root,data):
        if root is None:
            return False
        if root.data == data:
            return True
        
        if root.data<data:
            return self.searchHelper(root.right,data)
        
        return self.searchHelper(root.left,data)

    def search(self,data):
        return self.searchHelper(self.root,data)

    #For Counting
    def count(self):
        return self.numNodes
    
    #For Printing
    def printTreeHelper(self,root):
        if root is None:
            return
        print(root.data, end =':', sep='')
        
        if root.left!=None:
            print("L:",root.left.data,end=',',sep='')
        if root.right!=None:
            print("R:",root.right.data,end='',sep='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)

#main()
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
print(b.search(10))
print(b.search(7))
print(b.delete(4))
print(b.delete(10))

b.printTree()