
from sys import stdin

def checkRedundantBrackets(expression) :
    cnt=0
    s=list()
    close=')}'
    for ele in expression:
        if ele not in close:
            s.append(ele)
        elif ele in close:
            if ele==')':
                while s[-1]!= '(':
                    # print(s[-1])
                    s.pop()
                    cnt+=1
                s.pop()
                if cnt<=1:
                    return True
                cnt=0
            elif ele=='}':
                while s[-1]!='{':
                    s.pop()
                    cnt+=1
                s.pop()
                if cnt<=1:
                    return True
    
    if len(s)==0:
        return False

	





#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
