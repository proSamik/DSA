#order of opening and closing bracket matters
#LIFO strategy

# ')' = '('
# '}' = '{'
# ']' = '['
from sys import stdin

class Stack:

    def __init__(self):
        self.__data=[]
    
    def push(self,item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        else:    
            return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return -1
        return self.__data[len(self.__data)-1]
    
    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size()==0

def isBalanced(expression) :
    s= []
    
    for char in expression:

        if char in '{[(':
            s.append(char)
        elif char is ')':
            if(not s or s[-1]!='('):
                return False
            s.pop()
        elif char is ']':
            if(not s or s[-1]!='['):
                return False
            s.pop()
        elif char is '}':
            if(not s or s[-1]!='['):
                return False
            s.pop()
    
    if not s:
        return True

    return False
    
        
#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
