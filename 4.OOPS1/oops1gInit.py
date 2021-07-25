#init method

class Student:
    
    # def __init__(self):
    #     self.name = 'sab'
    #     self.rollNumber = 12

    def __init__(self,name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
# s1 = Student()
# s1.name= 'Ankush'
# s1.rollNumber = 12
# print(s1.__dict__)

# s2 = Student()
# s2.name= 'Rohan'
# s2.rollNumber = 13
# print(s2.__dict__)

s3 = Student ("Priya",14)
print(s3.__dict__)