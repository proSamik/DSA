#Tower of Hanoi 

def towerHanoi(n,a,b,c):
    if n==1:
        print("Move 1st disk from",a,"to",c)
        return
    
    towerHanoi((n-1),a,c,b)
    print("Move",n,"th disk from",a,"to",c)

    towerHanoi(n-1,b,a,c)

towerHanoi(4,"s","h","d")
