#Linked list note

class Node:

    # def __str__(self):
    #     return '''This is node class which stores two data:
    #     1. Data of value
    #     2. Reference of next Node object.
    #     This was is it
    #     '''

    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(13)
b=Node(15)

a.next = b

print(a.data)
print(b.data)
print(a.next.data)

print(a)