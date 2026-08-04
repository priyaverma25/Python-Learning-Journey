# def add(a, b):
#     return a + b


# class Math:
#     def __init__(self, num):
#         self.num = num
        
#     def addtonum(self, n):
#         self.num = self.num +n
        
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     # result = Math.add(1, 2)
#     # print(result) outpout: 3
#     a = Math(5)
#     print(a.num)
#     a.addtonum(6)
#     print(a.num)
    
#     print(a.add(7, 2))  
  
#  1: Basic Static Method 
  
class Student:
    
    @staticmethod
    def greet():
        print("Welcome to Python!")

Student.greet()

# Calling Through an Object

class Student:
    
    @staticmethod
    def greet():
        print("Welcome to Python!")

student = Student()
student.greet()

# 3: Static Method with Parameters

class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))
 
# 4: Utility Functions
 
class MathUtils:
    
    @staticmethod
    def square(num):
        return num * num

print(MathUtils.square(6))
 
 
  
    
# Instance vs classs varibles

class Student:
    def __init__(self, name):
        self.name 

 
 
 
 
 
 
 
 
 
 
class Student:
    school = "ABC School"

    @staticmethod
    def show_school():
        print(Student.school)

Student.show_school()
 
# 
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Priya", 20)
s2 = Student("Rahul", 21)

print(s1.name)
print(s2.name)
 
# Changing an Instance Variable 
class Student:
    
    def __init__(self, name):
        self.name = name

s1 = Student("Priya")
s2 = Student("Rahul")

s1.name = "Anjali"

print(s1.name)
print(s2.name)


# 
class Student:
    
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Priya")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)

# Changing a Class Variable

class Student:
    
    school = "ABC School"

Student.school = "XYZ School"

print(Student.school)

# Example with Both Variables

class Student:
    
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Priya")
s2 = Student("Rahul")

print(s1.name)
print(s1.school)

print(s2.name)
print(s2.school)
