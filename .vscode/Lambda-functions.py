# Lambda function-

# Add two number

add = lambda a, b : a+b
result = add(10, 20)
print("sum:", result)

# lambda with multile 

multiply = lambda a, b, c,: a*b*c
result = multiply(2, 3, 4)
print("product:", result)

# lambdawith one expression only
# vaid
square = lambda x:x**2
print(square(5)) # 25

# lambda with built-in Function

# using lambda with bult-in function
nums = [1, 2, 3, 4, 5]

# sort list in descending order
nums.sort(key = lambda x:x, reverse = True)
print(nums)

# map, filter and reduce in python

def cube(x):
    return x * x * x

print(cube(2))

l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#   newl.append(cube(item))

newl =list(map(cube, l))
print(newl)

# filter
# def filter_function(a):
#     return a>2

# newnewl = list(filter(filter_function, l))
# print(newnewl)

from functools import reduce

# list of numbers
numbers = [1, 2, 3, 4, 5]

# calculate the sum of the number using the reduce function

def mysum(x, y):
    return x + y

sum = reduce(sum, numbers)

# print the sum
print(sum)

