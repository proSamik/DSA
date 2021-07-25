# Check A and B
#abbaabb
def checkAB(a,si,ei):

    if si>ei:
        return True

    if a[0]!='a':
        return False
    
    smallCheck = checkAB(a,si+1,ei)

    print(f"{si}th index = {a[si]}")

    if si+1<=ei and a[si] == 'a':
        if a[si+1]=='a':

            print(f"cond= 1 1  val= {True and smallCheck}")
            return True and smallCheck

        elif si+2<=ei:

            if a[si+1:si+3]=='bb':

                print(f"cond= 1 2 1  val= {True and smallCheck}")
                return True and smallCheck
        else:

            print(f"cond= 1 3  val= {False}")
            return False

    elif a[si:si+2] =='bb':

        if si+2>ei:
            print(f"cond= 2 1  val= {True and smallCheck}")
            return True and smallCheck

        elif a[si+2]=='a':
            print(f"cond= 2 2  val= {True and smallCheck}")
            return True and smallCheck

        else:
            print(f"cond= 2 3  val= {False}")
            return False
    elif a[si]=='b' and a[si-1]=='b' and si+1<=ei:
        if a[si+1]=='a':
            print(f"cond= 2a 1  val= {True and smallCheck}")
            return True
        else:
            print(f"cond= 2b 2  val= {False}")
            return False
    else:
        if si == ei and a[si] == 'b':
            print(f"cond= 3 1  val= {True and smallCheck}")
            return True
        else:
            print(f"cond= 3 2  val= {False}")
            return False
    
    print('\n\n')
    

s = input()

if checkAB(s,0, len(s)-1):
    print("true")
else:
    print("false")