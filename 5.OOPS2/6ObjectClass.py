# Object Class

#by default every class inherits from object class

# __new__ __init__  __str__ comes default from object class

class Circle:
# class Circle(object):  both the definations are same 

    def __init__(self,radius):
        self.radius = radius

    def __str__(self):
        return '''This is a circle class which takes radus as an argument.'''

    #This is doc string

c = Circle(3)
print(c)