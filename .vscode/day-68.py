#  instance variables



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Priya", 20)
s2 = Student("Riya", 21)

print(s1.name)
print(s2.name)        

# class variables

class Student:
    college = "ABC College"
    
    def __init__(self, name, age):
        self.name = name
        
s1 = Student("Priya")
s2 = Student("Riya")

print(s1.college) 
print(s2.college) 
print(Student.college)      

