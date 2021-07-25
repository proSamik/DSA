# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    
    l=len(string)
    
    if l==0 or l==1:
        return string
    
    smallOutput = removeConsecutiveDuplicates(string[1:])

    if string[0]==string[1]:
        return str(smallOutput)

    else:
        return string[0] + str(smallOutput)   

# Main
from sys import setrecursionlimit
setrecursionlimit(3000)

string = input()
print(removeConsecutiveDuplicates(string))
