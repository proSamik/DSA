def printPairDiffK(l, k):
    d= {}
    count = 0
    
    for item in l:
        if item + k in d:
            count += d[item+k]

        if item-k in d:
            count += d[item-k]
        
        #Edge case
        #when element repeats itself
        if item - k == item:
            count -= d.get(item,0)
        
        d[item] = d.get(item,0) + 1
    
    return count
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))