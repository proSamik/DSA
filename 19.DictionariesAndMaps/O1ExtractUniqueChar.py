def uniqueChar(s): 
    d = {}
    for item in s:
        d[item] = d.get(item,0) + 1
    uniqueChar = ""
    for item in s:
        if d[item]>0:
            uniqueChar += str(item)
            d[item] = 0

    # print(d)
    return uniqueChar


# Main 
s=input() 
print(uniqueChar(s))