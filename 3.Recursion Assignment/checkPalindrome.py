#Check Palindrome using recursion

def palindromeRecursion(a):
    
    if len(a)==0 or len(a)==1:
        return True

    smallOutput= palindromeRecursion(a[1:-1])

    
    if a[0]== a[-1]:
        return (True and smallOutput)

    else:
        return (False and smallOutput)
    

a= input()

ans = palindromeRecursion(a)

if ans:
    print("true")
else:
    print("false")