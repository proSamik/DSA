#Method Resolution 


#ClassName.mro()
# will retrun the prefernce of class

#it follows the depth order 

#A(x,y) B(Y,z) M(B,A,z)

#the M.mro() will return order M > B > A >x >Y >z

class Mother:

    def __init__(self):
        self.name="Manju"

    def printC(self):

        print("Print of Mother called")

class Father:

    def __init__(self):
        self.name="Ajay"
        super().__init__()

    def printC(self):

        print("Print of Father called")

#Father's method will be given first priority in Child class instead of Mother

class Child(Father,Mother):

    def __init__(self,name):
        super().__init__()
    
    def printC(self):
        print("Name of child is",self.name)

c = Child("Rohan")
c.printC()

print(Child.mro())

