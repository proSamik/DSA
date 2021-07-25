#Protected Members

#It is declared with '_' single underscore before members

class Vehicle:

    def __init__(self,color,maxSpeed):
        self.color= color
        self._maxSpeed= maxSpeed

    #Getter function
    def getMaxSpeed(self):
        return self._maxSpeed
    
    #Setter function
    def setMaxSpeed(self,maxSpeed):
        self._maxSpeed = maxSpeed

    def printV(self):
        print("Color:",self.color)
        print("Maxspeed:",self._maxSpeed)

class Car(Vehicle):

    def __init__(self,color,maxSpeed,numGears,isConvertible):

        super().__init__(color,maxSpeed)

        self.numGears = numGears
        self.isConvertible= isConvertible

    def printV(self):
        # super().printV()
        print("NumGear:",self.numGears)
        print("IsConvertible:",self.isConvertible) 

# c= Car("red",15,3,False)
# c.printV()

v = Vehicle("red",18)
v.printV()

v._maxSpeed = 19
v.printV()

