
from sys import stdin

def isEmpty(s):
    return len(s)==0

def countBracketReversals(inputString) :
    cnt=0
    s=[]
    for char in inputString:

        if char=='{':
            s.append(char)
        
        elif char=='}':
            if isEmpty(s):
                s.append(char)
            
            elif not isEmpty(s) and s[-1]=='{':
                s.pop()
            elif not isEmpty(s) and s[-1]!='{':
                s.append(char)
    
    if len(s)%2!=0:
        return -1
    else:
        while len(s)!=0:
            c1=s.pop()
            c2=s.pop()
            if c1==c2 and (c1=='{' or c1=='}'):
                cnt+=1
            elif c1!=c2 and (c1=='}' or c1=='{'):
                cnt+=2

    return cnt


#main
print(countBracketReversals(stdin.readline().strip()))
