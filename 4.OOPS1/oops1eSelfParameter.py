#Instance method, using self

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
        
s1= Student()

s1.studentDetails()
Student.studentDetails(s1) 

#Both the above student object create with function refers the same

#className.function(objectName)

s1.isPassed()

