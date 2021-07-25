#Merge Sort

def mergeSort(a):

    print(f"UnsortedList=      {a} ")
    l =len(a)
    
    if l==0 or l==1:
        return a
    
    mid = (l)//2

    smallOutput1 = mergeSort(a[:mid])
    smallOutput2= mergeSort(a[mid:])

    # print(smallOutput1,'\n',smallOutput2)

    i=j=0

    lenA= len(smallOutput1)
    lenB= len(smallOutput2)

    # print(f"i= {i}   j={j}")
    # print(f"lenA={lenA}, lenB={lenB}")

    a= []

    while(i<lenA and j<lenB):

        if smallOutput1[i]==smallOutput2[j]:
            a.append(smallOutput1[i])
            a.append(smallOutput2[j])
            i+=1
            j+=1
        
        elif smallOutput1[i]<smallOutput2[j]:
            a.append(smallOutput1[i])
            i+=1
        
        elif smallOutput1[i]>smallOutput2[j]:
            a.append(smallOutput2[j])
            j+=1
        
    while(i<lenA):
        a.append(smallOutput1[i])
        i+=1
    while(j<lenB):
        a.append(smallOutput2[j])
        j+=1

    print(f"Sorted List {a}")

    return a

from sys import setrecursionlimit

setrecursionlimit(100)

a= [12,2,5,0,11,25,3]

print(a)

print(mergeSort(a))