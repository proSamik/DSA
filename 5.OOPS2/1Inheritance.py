#Basic of Inheritance

class Vehicle:

    def __init__(self,color,maxSpeed):
        self.color= color
        self.maxSpeed= maxSpeed


class Car(Vehicle):

    def __init__(self,color,maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)

        self.numGears = numGears
        self.isConvertible= isConvertible

    def printCar(self):
        print("Color:",self.color)
        print("Maxspeed:",self.maxSpeed)
        print("NumGear:",self.numGears)
        print("IsConvertible:",self.isConvertible) 

c= Car("red",15,3,False)
c.printCar()

