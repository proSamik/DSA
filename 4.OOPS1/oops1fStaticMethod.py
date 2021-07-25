#Static Method

class Student:
    passingPercentage =40

    def studentDetails(self):
        self.name= 'Samik'
        print("Name=", self.name)
        self.percentage= 80
        print("Percentage:",self.percentage)

    def isPassed(self):
        if self.percentage > Student.passingPercentage:
            print("Student is passed")
        else:
            print("Student is not passed")
    
    #Decorator, it will not bind this method with object
    #Static function doesn't require self by default    
    

    @staticmethod 
    def welcomeToSchool():
        print("Hey ! Welcome to School")

s1= Student()

s1.studentDetails()
Student.studentDetails(s1) 
s1.isPassed()

#We used decorator during definition

s1.welcomeToSchool()