# def average(a=9, b=1):
#     print("The average is ", (a+b)/2)
    
# # average(4, 6)
# average(b=9)

# # function to calculate simple interest

# def simple_interest(p, r, t):
#     return (p * r * t) / 100

# print(simple_interest(10000, 5, 2))


# # function to find largest element in list

# def largest(numbers):
#     max_num = numbers[0]

#     for num in numbers:
#         if num > max_num:
#             max_num = num

#     return max_num

# print(largest([5, 8, 2, 20, 12]))

# function to check palindrome

# def is_palindrome(text):
#     return text == text[::-1]

# print(is_palindrome("madam"))


# # function to find sum of list

# def list_sum(numbers):
#     total = 0

#     for num in numbers:
#         total += num

#     return total

# print(list_sum([1, 2, 3, 4, 5]))

# # functon to count vowels

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0

#     for ch in text:
#         if ch in vowels:
#             count += 1

#     return count

# print(count_vowels("Programming"))

#  baisc function
# A simple function with no argument and no return value.
def greet():
    print("Hello, World")
greet()
    
# function with parameters
#  A function that takes parameters.
def greet(name):
    print(f"Hello, {name}!")
greet("Akask")

# function with return value
# A function that returns a value.
def add(a, b):
    return a + b
result = add(6, 6)
print(result)

# function with default arguments
# A function with default parameter values.
def greet(name="World"):
  print(f"Hello, {name}!")
  
greet()
greet("Akash")  


# Recursion in python

def factorial(n):
    if(n==0 or n==1):
        return 1 
    else:
        return n * factorial(n-1)
    
    print(factorial(5))
    # 5 * factorial(4)
    # 5 * 4 * factorial(3)
    # 5 * 4 * 3 * factorial(2)
    # 5 * 4 * 3 * 2 * factorial(1)
    # 5 * 4 * 3 * 2 * 1 * factorial(0)
    f(0) = 0
    f(1) = 1
    f(2) = f(1) + f(0)
    f(n) = f(n-1) + f(n-2)