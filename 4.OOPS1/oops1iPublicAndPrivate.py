#Public and private access modifiers

#Public don't need any underscore '__'

#private needs '__' before variable name

#Name Hanglins used to access private members outside the class

#it replaces obj.__variable
#to obj._className__variable


class Student:

    passingPercentage =40

    def __init__(self,name,age=15,percentage=80):
        self.__name=name
        # self.__variableName  '___' makes it private
        self.age=age
        self.percentage = percentage
    
    def studentDetails(self):
        print("Name:",self.__name)
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

s1 = Student("Roshan")

print(s1.studentDetails())
s1.studentDetails()
#Name Hanglins
print(s1._Student__name)
