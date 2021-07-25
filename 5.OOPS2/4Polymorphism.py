#Method overriding

#Prefernce to Method of base class is given first as compared to super class. Bottom to top inheritance is preferred

#super() is used to call parent class specifically

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

    def printV(self):
        #self.printV()
        #Since we have printV() for both base and super class, we can't use self.printV() to call super class' printV() so we will use 'super()' keyword fun
        super().printV()
        print("NumGear:",self.numGears)
        print("IsConvertible:",self.isConvertible) 

c= Car("red",15,3,False)
c.printV()

