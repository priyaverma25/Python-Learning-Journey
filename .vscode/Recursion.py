# # Recursion
# def show(n):
#     if n == 0:   #  base case
#         return
#     print(n)
#     show(n - 1)     #  function calling itself
    
# show(5)

# #  types of recursion

# n = 5
# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1
    
# # diff types of case 

# def printNumbers(i, n):
#     if i > n:     # base case   
#         return
#     print(i, end=" ")     # recursive case
#     printNumbers(i + 1, n)
    
# printNumbers(1, 5)    

# 1 se N tak print
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)

print_numbers(5)

# N se 1 tak print
def reverse_count(n):
    if n == 0:
        return

    print(n)
    reverse_count(n - 1)

reverse_count(5)

# Sum of first N numbers
def total(n):
    if n == 0:
        return 0

    return n + total(n - 1)

print(total(5))

# Power of 3 check
def isPowerOfThree(n):
    if n <= 0:
        return False

    if n == 1:
        return True

    if n % 3 != 0:
        return False

    return isPowerOfThree(n // 3)

print(isPowerOfThree(27))