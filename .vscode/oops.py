def hello():
    print("hello")
    
hello()
sales1 = 6000
profit1 = 2000
ad1 = 1000
# rajeev.sales

sales2 = 6000
profit2 =2000
ad2 = 1000
# vikrant.sales

sales3 = 6000
profit = 2000
ad3 = 1000 

# RailwayForm ---> Class [blueprint]
# Harry  --> harry ki info wala format --> Object [entity]
# tom --> tom ki info wala from --> Object [entity]
# shubham --> shubhamki info wala form --> object [entity]
# shubham.changeName("Shubhi")


class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
a.name = "Shubham"
a.occuption = "Accountant"

b.name = "Nitika"
b.occupation = "HR"
# print(a.name, a.occupation)    
a.info()
b.info()


# constructors in python

class Person:
    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
        
    a = Person("Harry", "Developer") 
    b = Person("Divya", "HR")
    # c = Person(1, 2, 3)    
    a.info()
    b.info()   
    print(a.name)
    name = "Harry"
    

# Decorators in python










