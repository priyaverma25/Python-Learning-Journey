# def hello():
#     print("Hello world")
 
def greet(fx): 
  def mfx(*args, **Kwargs):
    print("Good Morning")  
    fx(*args, **Kwargs)
    print("thanks for using this function")
  return mfx

@greet    
def hello():
   print("Hello world")
          
def add(a, b):
    print(a+b)    
    
hello()    
greet(add)(1, 2)




