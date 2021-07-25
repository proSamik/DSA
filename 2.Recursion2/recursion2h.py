#Tower of Hanoi

def towerofhanoi(n, source, aux, dest):
    
    if n==1:
        print (source,dest)
    
    elif(n>0):
        towerofhanoi(n-1,source, dest, aux )

        print(source, dest)

        towerofhanoi(n-1, aux, source, dest)
    else:
        return

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')
