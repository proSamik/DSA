class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
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
        return self.printTreeHelper(self.root)
    
    def searchHelper(self,root,data):
        if root is None:
            return False
        
        if root.data == data:
            return True
        
        leftSearch = self.searchHelper(root.left,data)

        if leftSearch:
            return True
        
        return self.searchHelper(root.right,data)

    def search(self, data):
        if self.numNodes>0:
            return self.searchHelper(self.root,data)
        return False

    def insertHelper(self,root,data):
        if root is None:
            root = BinaryTreeNode(data)
            return root
        
        if data <= root.data:
            leftNode = self.insertHelper(root.left,data)
            root.left = leftNode
        if data> root.data:
            rightNode = self.insertHelper(root.right,data)
            root.right = rightNode
        
        return root

    def insert(self, data):
        if data==-1:
            return 
        self.root = self.insertHelper(self.root,data)
        self.numNodes+=1
    
    def minData(self,root):
        if root is None:
            return float("+inf")

        minLeft = self.minData(root.left)
        minRight = self.minData(root.right)

        return min(root.data,minLeft,minRight)

    def deleteHelper(self,root, data):
        if root is None:
            return None
        
        if root.data > data:
            leftSubTree  = self.deleteHelper(root.left,data)
            return leftSubTree
        
        if root.data < data: 
            rightSubTree = self.deleteHelper(root.right,data) 
            return rightSubTree
        
        else: 
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            m= self.minData(root.right)
            root.data = m
            root.right = self.deleteHelper(root.right,m)
            return root
                     
    def delete(self, data):
        result = self.deleteHelper(self.root,data)
        self.root = result
        self.numNodes-=1
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()