letter = 'Hey my name is {1} and I am from {0}'
country = 'India'
name = 'Harry'
print(letter.format(name, country))

price = 49.0999
txt = f"For only {price: 2f} dollars!"
print(txt)

print(type(f"{2 * 30}"))