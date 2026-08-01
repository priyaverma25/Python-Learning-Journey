

# class MyClass:
#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"Value is {self._value}")

#     @property
#     def ten_value(self):
#         return 10 * self._value

#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value / 10


# obj = MyClass(10)

# obj.ten_value = 67

# print(obj.ten_value)
# obj.show()

# without getter and setter
class Student:
    def __init__(self):
        self.name = "Priya"

s = Student()

print(s.name)
s.name = "Anjali"

print(s.name)

# using getter and setter methods
class Student:
    
    def __init__(self):
        self.__name = "Priya"

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

s = Student()

print(s.get_name())

s.set_name("Anjali")

print(s.get_name())

# getter and setter using @property
class Student:
    
    def __init__(self):
        self.__marks = 90

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        self.__marks = value

s = Student()

print(s.marks)

s.marks = 95

print(s.marks)

# Validation using setter
class Student:
    
    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value >= 0 and value <= 100:
            self.__marks = value
        else:
            print("Invalid Marks")

s = Student()

s.marks = 85
print(s.marks)

s.marks = 120








