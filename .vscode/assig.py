#  simple Calculator

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result =", num1 + num2)

elif op == "-":
     print("Result =", num1 - num2)

elif op == "*":
     print("Result =", num1 * num2)

elif op == "/":
     print("Result =", num1 / num2)

elif op == "%":
     print("Result =", num1 % num2)
else:
     print("Connot divide by zero")


     print("Invalid Operator")          

# # Quick Quiz

# nm = "Harry"
# print(nm[-4:-2])
# # Output: "ar"
# print(nm[3:5])
# # Output: "ry"

# # Time wishes problem

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


# even/odd 

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

# a = int(input())
# b = int(input())
# c = int(input())

# if a>b and a>c:
#     print(a) 
# elif b>a and b>c:          
#     print(b)
# else:
#     print(c)
      
# # Swap Without third variable 

# a = 10
# b = 20

# a,b = b,a

# print(a,b)


# # Divisible by 3 and 5

# num = int(input())
# if num%3==0 and num%5==0:
#     print("Yes")
# else:
#     print("No")
    
    
# # # Voting

# age = int(input())

# if age>=18:
#     print("Eligible")
# else:
#     print("Not Eligible")    

#  # Pass/Fail

# marks=int(input())

# if marks>=33:4

# print("Pass")
# else: 
# print("Fail")    

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
    
#     print(f"a. {questions[1]}       b. {questions[2]}")
#     print(f"c. {questions[3]}       d. {questions[4]}")
    
#     reply = int(input("Enter your answer (1-4)  "))
    
#     if(reply == questions[-1]):
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
      
# print(f"Your take home money is {money}")      
    