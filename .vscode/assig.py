# #  simple Calculator

# num1 = float(input("Enter first number: "))
# op = input("Enter operator (+, -, *, /, %): ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print("Result =", num1 + num2)

# elif op == "-":
#      print("Result =", num1 - num2)

# elif op == "*":
#      print("Result =", num1 * num2)

# elif op == "/":
#      print("Result =", num1 / num2)

# elif op == "%":
#      print("Result =", num1 % num2)
# else:
#      print("Connot divide by zero")


#      print("Invalid Operator")          

# # # Quick Quiz

# nm = "Harry"
# print(nm[-4:-2])
# # Output: "ar"
# print(nm[3:5])
# # Output: "ry"

# # # Time wishes problem

# import time
# t = time.strftime('%H:%M:%S')
# hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

# if(hour>0 and hour<12):
#     print("Good morning Sir!")
# elif(hour>=12 and hour<17):
#     print("Good Afternoon Sir!")
# elif(hour>=17 and hour<0):
#     print("Good Night sir!")       


# # even/odd 
# # 
# num = int(input("Enter number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("odd")
    
    
# # Leap Year

# year = int(input("Enter Year: "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not Leap Year")    


# # Largest of Three Numbers
 
# num1 = 10
# num2 = 25
# num3 = 15 

# if (num1 > num2 and num1 > num3):
#    print(num1)

# elif(num2 > num1 and num2 > num3):
#     print(num2)

# else:
#     print(num3)

# # Divisible by 3 and 5

# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print("Yes")
# else:
#     print("No")
    
    
#  # Voting

# age = int(input())

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")    

#  # Pass/Fail

# marks=int(input())

# if marks >= 33:
#    print("Pass")
# else: 
#    print("Fail")    

#  # Character Exists

# text="Python"

# if "P" in text:
#     print("Found")
# else:
#     print("Not Found")    

#  # kaun bane ga Crorepati

# questions = [
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript", 
#  "Php", "None", 4
#  ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#     ],
# ]

# levels = [1000, 2000, 3000, 5000, 1000, 2000, 4000, 8000, 16000, 32000]

# for i in range(0, len(questions)):
#     question = questions[i] 
    
#     print(f"\nQuestion for Rs. {levels[i]}")
    
#     print(f"1. {questions[1]}")      
#     print(f"3. {questions[2]}")
#     print(f"2. {questions[3]}")   
#     print(f"4. {questions[4]}")
    
#     reply = int(input("Enter your answer (1-4)  "))
    
#     if reply == questions[-1]:
#         print(f"Correct answer, you have won Rs. {levels[i]}")
#         if(i == 4):
#             money = 10000
#         elif(i == 9):
#             money = 320000
#         elif(i == 14):
#             money = 1000000        
#     else:
#         print("Wrong answer!")
#         break
      
# print(f"\nYour take home money is Rs. {money}")
    
# problem4
    
# st = input("Enter message")
# words = st.split(" ")
# coding = True
# if(coding):
#     nwords = []
#     for word in words:
#         if(len(word)>=3):
#             r1 = "dsf"
#             r2 = "jkr"
#             stnew = r1+ word[1:] + word[0] + r2 
#             nwords.append(stnew)
#         print(" ".join(nwords))
        
# else:
#     pass   




# # ATM Management System   

# balance = 10000
# pin = "1234"

# print("====== Welcome to ATM ======")

# entered_pin = input("Enter your 4-digit PIN: ")

# if entered_pin == pin:

#     while True:
#         print("\n===== ATM MENU =====")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             print(f"Your Balance is ₹{balance}")

#         elif choice == "2":
#             amount = float(input("Enter deposit amount: ₹"))
#             balance += amount
#             print("Money Deposited Successfully!")
#             print(f"Updated Balance = ₹{balance}")

#         elif choice == "3":
#             amount = float(input("Enter withdrawal amount: ₹"))

#             if amount <= balance:
#                 balance -= amount
#                 print("Please collect your cash.")
#                 print(f"Remaining Balance = ₹{balance}")
#             else:
#                 print("Insufficient Balance!")

#         elif choice == "4":
#             print("Thank you for using our ATM!")
#             break

#         else:
#             print("Invalid Choice!")

# else:
#     print("Incorrect PIN!")


# Number Guessing Game

# import random

# number = random.randint(1, 100)

# while True:
#     guess = int(input("Guess a number (1-100): "))

#     if guess < number:
#         print("Too Low!")
#     elif guess > number:
#         print("Too High!")
#     else:
#         print("Congratulations! You guessed it.")
#         break

# # Password Generator

# import random
# import string

# length = int(input("Enter password length: "))

# characters = string.ascii_letters + string.digits + string.punctuation
# password = "".join(random.choice(characters) for _ in range(length))

# print("Generated Password:", password)


# # QR Code Generator

# import qrcode

# data = input("Enter text or URL: ")

# img = qrcode.make(data)
# img.save("qrcode.png")

# print("QR Code generated successfully!")

# Dice Roller

# import random

# while True:
#     input("Press Enter to roll the dice...")
#     print("You got:", random.randint(1, 6))

#     again = input("Roll again? (yes/no): ").lower()
#     if again != "yes":
#         print("Game Over!")
#         break

# # Countdown Timer 

# import time

# seconds = int(input("Enter time in seconds: "))

# while seconds:
#     print(seconds)
#     time.sleep(1)
#     seconds -= 1

# print("Time's Up!")

# Random Quote Generator

# import random
# quotes = [
#     "Never Give Up!",
#     "Believe in Yourself.",
#     "Success Comes from Consistency.",
#     "Keep learing Every Day."
# ]

# print(random.choice(quotes))

# # Digital Stopwatch

# import time
# input("Press Enter to Start")
# start = time.time()
# input("Press Enter to step")
# end = time.time()

# print("Elapsed Time:", round(end - start, 2), "seconds")

# # Age Calculator

# from datetime import date

# birth = int(input("Enter Birth Year: "))
# current = date.today().year

# print("Your Age is:", current - birth)

# Check Armstrong Number

# num = int(input("Enter a number: "))

# temp = num
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total += digit ** 3
#     temp //= 10

# if total == num:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")
    
# # Find Maximum Number    
    
# numbers = [10, 45, 23, 89, 5]

# print("Largest Number:", max(numbers))  

# # Count Even and Odd Numbers  

# numbers = [10, 15, 8, 21, 30, 7]

# even = 0
# odd = 0

# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even:", even)
# print("Odd:", odd)

# # Fibonacci Series

# n = int(input("How many terms? "))

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# Factorial

# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print("Factorial =", fact)

# # Sum of Digits

# num = input("Enter a number: ")

# total = 0

# for digit in num:
#     total += int(digit)

# print("Sum of Digits:", total)

# # Count Vowels

# text = input("Enter a word: ").lower()

# count = 0

# for ch in text:
#     if ch in "aeiou":
#         count += 1

# print("Total Vowels:", count)

# # Reverse a String

# text = input("Enter a string: ")

# print("Reversed String:", text[::-1])

# # Multiplication Table

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")                                                                                                           


# # Geekforgeeks

# n = int(input())

# # code here
# if n % 3 == 0 and n % 5 == 0:
 
#   print("FizzBuzz")

# elif n % 3 == 0:
    
#     print("Fizz")

# elif n % 5 == 0:
    
#     print("Buzz")

# else:
#     print(n)

# problem

# x = [1, 2, 3]
# y = x[:]
# y.append(4)
# print(x)

# # 
# str1 = 'Python'
# str2 = str1[2:]+str1[:2]
# print(str1 in 2*str2)

# #
 
# def fun():
#     for x in range(22, 23, 24)
#     print(x)
# fun()

# #

# Dict = {1:2, 3:4}
# for i, j in Dict.items():
#     print(i, j, sep=":") 
    
# #

# name1 = "Dhoni"
# name2 = "Kohli"
# result = name1[:3] + name2[1:]
# print(result)

# # 

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# result = list(zip(list1, list2))
# print(result) 

# # 

# a = 32 * 19
# b = 175 * 3 - 5

# if b >= a:
#    print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")    

# library management system

# class Library:
#     def __init__(self):
#         self.nobooks = 0
#         self.books = []
        
#     def addBook(self, book):
#         self.books.append(book)
#         self.nobooks = len(self.books)
             
#     def showInfo(self):
#       print(f"The library has {self.nobooks} books. The books are")
#       for book in self.books:
#           print(book)

# li = Library()
# li.addBook("Harry Potter1")
# li.addBook("Harry Potter2")
# li.addBook("Harry Potter3")
# li.showInfo()       


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print("Hello", name)
# print("Your age is", age)

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# # 1. Hello World
# print("Hello World")

# # 2. Variables
# name = "Rahul"
# age = 18

# print("Name:", name)
# print("Age:", age)

# # 3. User input
# name = input("अपना नाम लिखें: ")
# print("Hello", name)

# # 4. Addition
# number1 = int(input("पहला number: "))
# number2 = int(input("दूसरा number: "))

# total = number1 + number2
# print("Total:", total)

# # 5. If-else
# number = int(input("एक number लिखें: "))

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# # 6. For loop
# for number in range(1, 6):
#     print(number)

# # 7. While loop
# number = 1

# while number <= 5:
#     print(number)
#     number += 1

# # 8. List
# fruits = ["Apple", "Banana", "Mango"]

# for fruit in fruits:
#     print(fruit)

# # 9. Function
# def add(a, b):
#     return a + b

# result = add(10, 20)
# print("Result:", result)

# Student Result System

# def calculate_total(marks):
#     return sum(marks)


# def calculate_percentage(total, number_of_subjects):
#     return total / number_of_subjects


# def find_grade(percentage):
#     if percentage >= 90:
#         return "A+"
#     elif percentage >= 80:
#         return "A"
#     elif percentage >= 70:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     elif percentage >= 50:
#         return "D"
#     else:
#         return "F"


# print("===== STUDENT RESULT SYSTEM =====")

# student_name = input("Student का नाम लिखें: ")
# roll_number = input("Roll number लिखें: ")

# subjects = ["Hindi", "English", "Math", "Science", "Computer"]
# marks = []

# # प्रत्येक subject के marks लेना
# for subject in subjects:
#     while True:
#         mark = int(input(f"{subject} के marks लिखें (0-100): "))

#         if 0 <= mark <= 100:
#             marks.append(mark)
#             break
#         else:
#             print("Marks केवल 0 से 100 के बीच लिखें।")

# # Result calculate करना
# total = calculate_total(marks)
# percentage = calculate_percentage(total, len(subjects))
# grade = find_grade(percentage)

# # प्रत्येक subject में pass check करना
# is_pass = True

# for mark in marks:
#     if mark < 33:
#         is_pass = False
#         break

# # Result दिखाना
# print("\n===== RESULT =====")
# print("Student Name:", student_name)
# print("Roll Number:", roll_number)
# print("----------------------------")

# for index in range(len(subjects)):
#     print(subjects[index], ":", marks[index])

# print("----------------------------")
# print("Total Marks:", total, "/", len(subjects) * 100)
# print("Percentage:", round(percentage, 2), "%")
# print("Grade:", grade)

# if is_pass:
#     print("Result: PASS")
# else:
#     print("Result: FAIL")

# # Highest और lowest marks
# highest_marks = max(marks)
# lowest_marks = min(marks)

# highest_index = marks.index(highest_marks)
# lowest_index = marks.index(lowest_marks)

# print("\nHighest Marks:", highest_marks)
# print("Highest Subject:", subjects[highest_index])

# print("Lowest Marks:", lowest_marks)
# print("Lowest Subject:", subjects[lowest_index])

# print("\n===== PROGRAM FINISH =====")

# Sum of Digits
# num = int(input("Enter a number: "))

# total = 0

# while num > 0:
#     digit = num % 10
#     total = total + digit
#     num = num // 10

# print("Sum of digits:", total)       
        
# # Count Vowels        
# text = input("Enter a string: ")

# count = 0

# for char in text:
#     if char.lower() in "aeiou":
#         count += 1

# print("Number of vowels:", count)


# # Reverse a Number
# num = int(input("Enter a number: "))

# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reversed number:", reverse)

# Largest Number Without max()
numbers = [12, 45, 7, 89, 34, 23]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)

# Palindrome Checker
word = input("Enter a word: ")

reverse = word[::-1]

if word.lower() == reverse.lower():
    print("Palindrome")
else:
    print("Not Palindrome")