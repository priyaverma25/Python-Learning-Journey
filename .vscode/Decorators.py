# def hello():
#     print("Hello world")

# Basic Syntax of Decorators
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def hello():
    print("Hello Priya!")
   
   
# without using @decorator syntax 
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def hello():
    print("Hello")

hello = decorator(hello)

hello()  

# Decorators with arguments
def decorator(func):
    def wrapper(name):
        print("Welcome")
        func(name)
        print("Thank You")
    return wrapper

@decorator
def greet(name):
    print("Hello", name)

greet("Priya")  
    
# Decorators with *args and **kwargs

# hello()
# def greet(fx): 
#   def mfx(*args, **Kwargs):
#     print("Good Morning")  
#     fx(*args, **Kwargs)
#     print("thanks for using this function")
#   return mfx

# @greet    
# def hello():
#    print("Hello world")
          
# def add(a, b):
#     print(a+b)    
    
# hello()    
# greet(add)(1, 2)

# returning values from decorators

def decorator(func):
    def wrapper():
        return func() * 2
    return wrapper

@decorator
def number():
    return 5

print(number())

# Multiple decorators
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Python"

print(text())





