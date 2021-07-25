#Creating dictionary

# manually
a = {"the":1,"a":5, 10000: "abc"}
print(type(a))
print(a)

#Copying
b= a.copy()
print(b)

#key value pair in list
c= dict([("the",3),("a",10),(2,3)])
print(c)

#fromkeys
d= dict.fromkeys(["abc",32,4],10)
print(d)