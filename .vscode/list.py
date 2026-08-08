


# List बनाना
fruits = ["apple", "mango", "banana"]

# पूरी list दिखाना
print(fruits)

# एक item दिखाना
print(fruits[0])  # apple

# नया item जोड़ना
fruits.append("orange")

# item हटाना
fruits.remove("mango")

# सभी items दिखाना
for fruit in fruits:
    print(fruit)# Create a List

from ast import Add, List
from xml.etree.ElementTree import Element


fruits = ["Apple", "Banana", "Mango", "Orange"]
print(fruits)

# Access List Elements

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])    
print(fruits[2])    
print(fruits[-1])   

# Change List Element

fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Grapes"

print(fruits)

# Add Elements

fruits = ["Apple", "Banana"]
fruits.append("Mango")
fruits.insert(1, "Orange")

print(fruits)

# Remove Elements

fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Banana")
fruits.pop(0)
del fruits[0]
print(fruits)

# List length

numbers = [10, 20, 30, 40, 50]
print(len(numbers))

# Sort List

numbers = [50, 30, 10, 40, 20]
numbers.sort()
print(numbers)

# Reverse List

numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

# Copy List

list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)

