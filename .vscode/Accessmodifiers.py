# # 1. Public Members

# class Student:
#     def __init__(self, name):
#         self.name = name       # Public variable

#     def display(self):         # Public method
#         print("Name:", self.name)


# student = Student("Priya")

# print(student.name)   # Allowed
# student.display()     # Allowed

# # Protected Members

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self._marks = marks       # Protected variable

#     def _show_marks(self):        # Protected method
#         print("Marks:", self._marks)


# student = Student("Priya", 85)

# print(student._marks)      # Possible, but not recommended
# student._show_marks()      # Possible, but not recommended

# # Protected member with inheritance

# class Student:
#     def __init__(self, marks):
#         self._marks = marks


# class Result(Student):
#     def show_result(self):
#         print("Marks:", self._marks)


# result = Result(90)
# result.show_result()

# # Private Members

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance       # Private variable

#     def __show_balance(self):          # Private method
#         print("Balance:", self.__balance)

#     def display(self):
#         self.__show_balance()


# account = BankAccount(5000)

# account.display()             # Allowed
# # print(account.__balance)    # AttributeError
# # account.__show_balance()    # AttributeError


# # Accessing Private Data Correctly

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Balance cannot be negative")


# account = BankAccount(5000)

# print(account.get_balance())

# account.set_balance(7000)
# print(account.get_balance()) 

# Instance Variables vs Class Variables in Python

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

# Example

class Student:
    
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Priya")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)

