# String to Integer

def strToInt(s,si):

    l= len(s)

    if l==0 or si>l-1:
        return 0
    
    smallOutput= strToInt(s,si+1)

    val = int(s[si])
    val = val*(10**(l-si-1))

    return val + smallOutput

s= input()

print(strToInt(s,0))