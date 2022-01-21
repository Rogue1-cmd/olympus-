#python calculator app
#defining functions

def add(x , y):
    z = round((x + y), 4)
    print("\nThe sum of the two numbers is,", z)
    return str(x) + ' + ' + str(y) + ' = ' + str(z)
    
def subtract(x , y):
    z = round((x - y), 4)
    print("\nThe difference of the two numbers is,", z)
    return str(x) + ' - ' + str(y) + ' = ' + str(z)
    
def multiply(x , y):    
    z = round((x * y), 4)
    print("\nThe product of the two numbers is,", z)
    return str(x) + ' * ' + str(y) + ' = ' + str(z)    

def divide(x, y):    
    if y != 0:
        z = round((x/y), 4)
        print("\nThe quotient of the two numbers is,", z)
        return str(x) + ' / ' + str(y) + ' = ' + str(z)
    elif y == 0:
        print("\nYou cannot divide by zero!!!")
        return ("\nDIV ERROR!!!")
    
def exponent(x, y):    
    z = round((x**y), 4)
    print(x, "raised to the power of", y, "is", z)
    return str(x) + ' ** ' + str(y) + ' = ' + str(z)
   
print("This is a calculator.")
history = []

active = True
while active:
    x = int(input("\nEnter first number: "))
    y = int(input("Enter second number: "))
    op = input("\nEnter operation(addition, subtraction, multiplication, division, or exponentiation): \n\t\t").lower()
    if op.startswith('a'):
        z = add(x, y)       
    elif op.startswith("s") :        
        z = subtract(x,y)       
    elif op.startswith("m"):        
        z = multiply(x,y)        
    elif op.startswith("d"):
        z = divide(x,y)   
    elif op.startswith("e"):        
        z = exponent(x,y)               
    else :
        print("OPP ERROR!!!") 

    history.append(str(z))          
        
    choice = input("\nWould you like to continue? (y/n): \t").lower()        
    if choice != "y":
        print("\n\t---------SUMMARY---------")
        for i in history:
            print("\t ", i)
        active = False 
        print("Okay, bye.")




