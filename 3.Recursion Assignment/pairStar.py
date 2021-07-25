#Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

def pairStar(a,si,ei):

    if si==ei:
        return a[si]
    
    if a[si] == a[si+1]:
        smallOuptut = pairStar(a,si+1,ei)

        pair = a[si] + "*"

        return pair + smallOuptut
    else:
        smallOuptut = pairStar(a,si+1,ei)

        return a[si] + smallOuptut

s = input()

print(pairStar(s,0,len(s)-1))
    