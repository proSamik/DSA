#Class Methods
from datetime import date


class Student:

    passingPercentage =40

    def __init__(self,name,age=15,percentage=80):
        self.name=name
        self.age=age
        self.percentage = percentage
    
    #returning factory methods
    #it returns object
    @classmethod
    def fromBirthYear(cls,name,year,percentage):
        age= date.today().year-year
        return cls(name,age, percentage)


    def studentDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Percentage:",self.percentage)
        
    
    def isPassed(self):

        if self.percentage> Student.passingPercentage:
            print("Student is passed")
        else:
            print("Student is not passed")

    
    #it is a utility function
    @staticmethod
    def welcomeToSchool():
        print("Hey! Welcome to School")

    @staticmethod
    def isTeen(age):
        return age>16

s1 = Student("Roshan")

s2 = Student.fromBirthYear("Parikh",2001,70)

print(s2.studentDetails())