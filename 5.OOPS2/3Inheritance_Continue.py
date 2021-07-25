#Inheritance Continue

#The responsibility of printing super class members are it's methods not a derived class should do it.

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

    def printV(self):
        print("Color:",self.color)
        print("Maxspeed:",self.__maxSpeed)

class Car(Vehicle):

    def __init__(self,color,maxSpeed,numGears,isConvertible):
        super().__init__(color,maxSpeed)

        self.numGears = numGears
        self.isConvertible= isConvertible

    def printCar(self):
        super().printV()  
        # self.printV() will also work
        print("NumGear:",self.numGears)
        print("IsConvertible:",self.isConvertible) 

c= Car("red",15,3,False)
c.printCar()

