# s = {2, 4, 2, 6}
# print(s)

# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# priya = set()
# print(type(priya))

# # union() and update()
# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1, s2)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# cities3 =cities.update(cities2)
# print(cities3)

# # intersection and intersection_update()
# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.intersection(s2))
# s1.intersection.update(s2)
# print(s1, s2)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# cities3 =cities.intersection_update(cities2)
# print(cities3)

# # symmetric_difference and symmetric_difference_update()
# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.symmetric_difference(s2))
# s1.symmetric_differenceupdate(s2)
# print(s1, s2)


# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
# cities3 =cities.symmetric_difference_update(cities2)
# print(cities3)

# # difference() and difference_update():
# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.difference(s2))
# s1.difference.update(s2)
# print(s1, s2)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.difference(cities2)
# cities3 =cities.difference_update(cities2)
# print(cities3)

# # isdisjiont()
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.isdisjoint(cities2)


# # issuperset():
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.isdisjoint(cities2)


# # del
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# Small Challenge

numbers = set()

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.add(num)

print("Unique numbers:", numbers)

# Python Set Practice Problems
# Author: Priya Verma

# 1. Creating a set
numbers = {10, 20, 30, 40, 50}
print("Original set:", numbers)


# 2. Removing duplicate values from a list
values = [10, 20, 10, 30, 20, 40]

unique_values = set(values)
print("Unique values:", unique_values)


# 3. Adding an element
numbers.add(60)
print("After adding 60:", numbers)


# 4. Removing an element
numbers.remove(20)
print("After removing 20:", numbers)


# 5. Checking whether an element exists
languages = {"Python", "Java", "C++"}

if "Python" in languages:
    print("Python is present in the set")
else:
    print("Python is not present in the set")


# 6. Union of two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union_result = set_a.union(set_b)
print("Union:", union_result)


# 7. Intersection of two sets
intersection_result = set_a.intersection(set_b)
print("Intersection:", intersection_result)


# 8. Difference between two sets
difference_result = set_a.difference(set_b)
print("Difference (A - B):", difference_result)


# 9. Symmetric difference
symmetric_difference = set_a.symmetric_difference(set_b)
print("Symmetric difference:", symmetric_difference)


# 10. Taking numbers from the user
user_numbers = set()

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    user_numbers.add(number)

print("Unique numbers entered by user:", user_numbers)



