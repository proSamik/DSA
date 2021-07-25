#Inheritance and private members

#To access the private members of super class we do it by getter and setter function

class Vehicle:

    def __init__(self,color,maxSpeed):
        self.color= color
        self.__maxSpeed= maxSpeed

    #Getter function
    def getMaxSpeed(self):
        return self.__maxSpeed
    
    #Setter function
    def setMaxSpeed(self,maxSpeed):
        self.__maxSpeed = maxSpeed

class Car(Vehicle):

    def __init__(self,color,maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)

        self.numGears = numGears
        self.isConvertible= isConvertible

    def printCar(self):
        print("Color:",self.color)
        print("Maxspeed:",self.getMaxSpeed())
        print("NumGear:",self.numGears)
        print("IsConvertible:",self.isConvertible) 

c= Car("red",15,3,False)
c.printCar()

