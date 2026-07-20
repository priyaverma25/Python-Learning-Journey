# readlines

f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
    

f = open('myfile.txt', 'r')
contents = f.read()
print(contents)

f = open('myfile.txt', 'r')
while True: 
    line = f.readline()
    if not line:
        break
    print(line)
    
    f = open('myfile.txt', 'r')
    f.write("Hello, world!")
    f.Close()
    
with open('myfile.txt', 'r') as f:
    f.write("Hey I am inside with")



# Writeline() method

f = open('myfile.txt', 'w')
line = ['line1\n', 'line2\n', 'line3\n'] 
f.writelines(lines)
f.close()

f = open('myfile.txt', 'w')
f.write('Hello, world!')


# seek() function-

f = open("data.txt", "r")
print(f.read(5)) # read first
# 5 characters

f.seek(0) # move cursor
# to the beginning

print(f.read (5))
f.close()

# tell() function

f = open("data.txt", 'r')
print(f.tell())  # 0
f.read(5)
print(f.tell()) # 5
f.close()

# Using seek() and tell() together

f = open("data.txt", 'r')
print(f.tell()) # 0
f.read(5)
print(f.tell()) # 5
f.seek(0)
print(f.tell()) # 0
f.colse()



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    