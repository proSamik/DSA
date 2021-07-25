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
    s= Stack()
    size=len(expression)
    for i in range(size):
        ele = expression[i]
        if ele == '(' or ele == '{' or ele=='[':
            s.push(ele)
            # print(s.top())
        elif ele== ')' or ele== '}' or ele == ']':
            if ele == ']':
                if s.top() == '[':
                    s.pop()
                else:
                    return False
            elif ele == '}':
                if s.top() == '{':
                    s.pop()
                else:
                    return False
            elif ele == ')':
                # print(ele, 'pair=',s.top())
                if s.top() == '(':
                    s.pop() 
                else:
                    return False

    if s.isEmpty():
        return True
    else:
        False
    
        



#main
expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")
