# Recursion
def show(n):
    if n == 0:   #  base case
        return
    print(n)
    show(n - 1)     #  function calling itself
    
show(5)

#  types of recursion

n = 5
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
    
# diff types of case 

def printNumbers(i, n):
    if i > n:     # base case   
        return
    print(i, end=" ")     # recursive case
    printNumbers(i + 1, n)
    
printNumbers(1, 5)    
    