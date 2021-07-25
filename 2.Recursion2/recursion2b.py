# Remove pi with 3.14

def replacePi(s):

    l= len(s)

    if l==0 or l==1:
        return s
    
    if s[0:2] == 'pi':
        smallOutput = replacePi(s[2:])
        return '3.14' + smallOutput
    else:
        smallOutput = replacePi(s[1:])
        return s[0] + smallOutput

print(replacePi('abcpiabdpiabdpplpicdpei'))

print(replacePi('pippi'))

