

# # Creating a tuple
# fruits = ("Apple", "Banana", "Mango", "Orange")

# print("Tuple:", fruits)

# # Accessing elements
# print("First Fruit:", fruits[0])
# print("Last Fruit:", fruits[-1])

# # Tuple length
# print("Total Fruits:", len(fruits))

# # Loop through tuple
# print("\nFruits List:")
# for fruit in fruits:
#     print(fruit)

# # Checking an item
# if "Mango" in fruits:
#     print("\nMango is available in the tuple.")

# Access Tuple Elements

colors = ("Red", "Green", "Blue")
print(colors[0])   # Red
print(colors[1])   # Green
print(colors[-1])  # Blue 

# Tuple Slicing

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])  # (20, 30, 40)
print(numbers[:3])   # (10, 20, 30)
print(numbers[::2])  # (10, 30, 50)

# Single-Element Tuple

value = (10,)
print(type(value))  # <class 'tuple'>

# Loop Through a Tuple

fruits = ("Apple", "Mango", "Banana")
for fruit in fruits:
    print(fruit)

# Check Item Exists

fruits = ("Apple", "Mango", "Banana")
if "Mango" in fruits:
    print("Mango is present")

