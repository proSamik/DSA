# Check A & B 

def checkAB(a,si,ei):

    if si>ei:
        return True
    
    if a[0]!='a':
        return False
    
    smallCheck = checkAB(a,si+1,ei)

    if a[si] == 'a':
        if si==ei:
            return True

        elif a[si+1] == 'a':
            return True and smallCheck

        elif si+2<=ei:
            if a[si+1:si+3]=='bb':
                return True and smallCheck

    elif a[si] == 'b':
        if a[si-1]=='b':
            if si==ei:
                return True and smallCheck
            elif a[si+1]=='a':
                return True and smallCheck

        elif a[si-1]=='a':
            if si==ei:
                return False
            
            elif a[si+1]=='b':
                return True and smallCheck
        
    return False

s = input()

if checkAB(s,0, len(s)-1):
    print("true")
else:
    print("false")