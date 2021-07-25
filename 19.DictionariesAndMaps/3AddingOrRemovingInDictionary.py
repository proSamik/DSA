a = {1:2, 2:4, "list":[1,23], "dict":{1:2}}

#Adding is straight forward
a['tuple'] = (1,2,3)
print(a)

#updating is also straight forward
a[1]=10
print(a)

#updating data from other dictionary
b = {1:5, "the":4, 2:100}
a.update(b)
print(a)

#Delete element from dictionary by key
a.pop('tuple')
print(a)

#Delete from key
del a[1]
print(a)

#Clear the dictionary
a.clear()
print(a)

#Delete the dictionary
del a 
print(a)