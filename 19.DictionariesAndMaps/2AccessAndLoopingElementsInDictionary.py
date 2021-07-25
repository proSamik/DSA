a = {1:2, 2:4, "list":[1,23], "dict":{1:2}}
print(a)

print(a['list'])

print(a.get('li'))

print(a.get('li',0))

print(a.keys())

print(a.values())

print(a.items())

for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

#If some key exist in my dictionary
print("list" in a)