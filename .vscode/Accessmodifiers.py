# 1. Public Members

class Student:
    def __init__(self, name):
        self.name = name       # Public variable

    def display(self):         # Public method
        print("Name:", self.name)


student = Student("Priya")

print(student.name)   # Allowed
student.display()     # Allowed

# Protected Members

class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks       # Protected variable

    def _show_marks(self):        # Protected method
        print("Marks:", self._marks)


student = Student("Priya", 85)

print(student._marks)      # Possible, but not recommended
student._show_marks()      # Possible, but not recommended

# Protected member with inheritance

class Student:
    def __init__(self, marks):
        self._marks = marks


class Result(Student):
    def show_result(self):
        print("Marks:", self._marks)


result = Result(90)
result.show_result()

# Private Members

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance       # Private variable

    def __show_balance(self):          # Private method
        print("Balance:", self.__balance)

    def display(self):
        self.__show_balance()


account = BankAccount(5000)

account.display()             # Allowed
# print(account.__balance)    # AttributeError
# account.__show_balance()    # AttributeError


# Accessing Private Data Correctly

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")


account = BankAccount(5000)

print(account.get_balance())

account.set_balance(7000)
print(account.get_balance())