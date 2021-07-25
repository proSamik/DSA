# Replace some character with another using recursion

def replaceChar(a,char1,char2):

    l =len(a)

    if l==0:
        return a

    else:
        smallestStr = a[1:]
        smallestStr= replaceChar(smallestStr,char1,char2)

        if a[0] == char1:
            return char2 + smallestStr
        else:
            return a[0] + smallestStr
    
a = 'dacdxcd'

print(replaceChar(a,'c','x'))


	
    
