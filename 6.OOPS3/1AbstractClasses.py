#Abstract classes 
# 
# It contains abstract methods

#These are declared but they have no implentation

#Object of abstract class cannot be created

#Implement all the abstract method in the child class

#@abstractmethod if we have any of this before method we cannot create object of that class

#In python ABC is class which is inherited to use the @abstractmethod

from abc import ABC, abstractmethod

class Automobile(ABC):

    def __init__(self):
        print("Automobile Created")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Automobile):

    def __init__(self,name):

        print("Car created")
        self.name = name

    def start(self):
        pass
    
    def stop(self):
        pass

    def drive(self):
        pass

class Bus(Automobile):

    def __init__(self,name):
        print("Bus created")
        self.name = name

c =Car("Honda")

b= Bus("Delhi")

