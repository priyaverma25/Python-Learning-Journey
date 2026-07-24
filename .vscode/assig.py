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

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))

    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("Congratulations! You guessed it.")
        break

# Password Generator

import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)


# QR Code Generator

import qrcode

data = input("Enter text or URL: ")

img = qrcode.make(data)
img.save("qrcode.png")

print("QR Code generated successfully!")






