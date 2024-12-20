#Abstract classes continue
 
from abc import ABC, abstractmethod

class Automobile(ABC):

    def __init__(self, no_of_wheels):

        self.no_of_wheels = no_of_wheels
        print("Automobile Created")

    @abstractmethod
    def start(self):
        print("Start of Automobile called")

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def get_no_of_wheels(self):
        return self.no_of_wheels

class Car(Automobile):

    def start(self):
        super().start()
        print("Start of Car called")
    
    def stop(self):
        pass

    def drive(self):
        pass

    def get_no_of_wheels(self):
        return super().get_no_of_wheels()

class Bus(Automobile):

    def start(self):
        pass
    
    def stop(self):
        pass

    def drive(self):
        pass

    def get_no_of_wheels(self):
        return super().get_no_of_wheels()

c =Car(4)

print(c.get_no_of_wheels())

b = Bus(10)

print(b.get_no_of_wheels())

