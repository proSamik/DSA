def subsetSum(l):
    maxLength = 0
    sumOfEle = 0
    d = {0: -1}
    size = len(l)
    for i in range(size):
        ele = l[i]
        sumOfEle += ele

        if sumOfEle in d:
            subsetSize = d[sumOfEle-ele] - d[sumOfEle] + 1
            if subsetSize > maxLength:
                maxLength = subsetSize
        else:
            d[sumOfEle] = i

    return maxLength 


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))