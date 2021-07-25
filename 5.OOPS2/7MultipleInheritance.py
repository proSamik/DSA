#Multiple Inheritance

#The order of method depends on order of inheritance is done a1,a2,a3 are base class inherited then a1's first base class is preferred 


class Mother:

    def __init__(self):
        self.name="Manju"

    def print(self):

        print("Print of Mother called")

class Father:

    def __init__(self):
        self.name="Ajay"

    def print(self):

        print("Print of Father called")

#Father's method will be given first priority in Child class instead of Mother

class Child(Father,Mother):

    def __init__(self,name):
        super().__init__()
        self.name = name
    
    def printChild(self):
        print("Name of child is",self.name)

c = Child("Rohan")
c.print()
c.printChild()

