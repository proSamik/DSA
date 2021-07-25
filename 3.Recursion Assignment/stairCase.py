#A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.

def stairCase(n):

    if n==1 or n==0:
        return 1
    
    elif n==2:
        return 2
    
    else:
        return stairCase(n-3) + stairCase(n-2) + stairCase(n-1)


n = int(input())

w = stairCase(n)

print(w)