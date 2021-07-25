class Student:
    # name = ""
    # rollNumber= 12

    pass
     

s1 = Student()
s2 = Student()
s3 = Student()

print(s1)

s1.name = 'Ankush'

s2.rollNumber = 12

s3.name = 'Rohan'
s3.rollNumber =13

print(s1.name)

print( s1.__dict__  )

print( s2.__dict__  )

print( s3.__dict__  )


print( hasattr(s1,"name") )

print( hasattr(s2,"name") )

print( getattr(s1,"name") )

print( getattr(s2,"name","empty") )

delattr(s1,'name')

print(s1.__dict__)