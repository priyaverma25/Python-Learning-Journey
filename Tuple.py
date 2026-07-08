

# Creating a tuple
fruits = ("Apple", "Banana", "Mango", "Orange")

print("Tuple:", fruits)

# Accessing elements
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Tuple length
print("Total Fruits:", len(fruits))

# Loop through tuple
print("\nFruits List:")
for fruit in fruits:
    print(fruit)

# Checking an item
if "Mango" in fruits:
    print("\nMango is available in the tuple.")
