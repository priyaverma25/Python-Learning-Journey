s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

priya = set()
print(type(priya))

# union() and update()
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
cities3 =cities.update(cities2)
print(cities3)

# intersection and intersection_update()
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.intersection(s2))
s1.intersection.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
cities3 =cities.intersection_update(cities2)
print(cities3)

# symmetric_difference and symmetric_difference_update()
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.symmetric_difference(s2))
s1.symmetric_differenceupdate(s2)
print(s1, s2)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
cities3 =cities.symmetric_difference_update(cities2)
print(cities3)

# difference() and difference_update():
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.difference(s2))
s1.difference.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.difference(cities2)
cities3 =cities.difference_update(cities2)
print(cities3)

# isdisjiont()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)


# issuperset():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.isdisjoint(cities2)


# del
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)




