a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
 for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invaid Input!") 
       
    
print("Some lines of code")
print("End of program")    


# finally key word 

    
try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    
except:
    print("Some error occurred:")

finally:
    print("I am always executed")

