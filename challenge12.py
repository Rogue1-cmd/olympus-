#Quadratic equation solver
import cmath
import time


print("\tWelcome to the quadratic equation solver! \n A quadratic equation is of the for ax^2+bx+c=0 \n")
print("Solution can be real or complex")


prompt = int(input("How many quadratic equations would you like to solve?:\n"))
quad_values = []
round = 0
for i in range(prompt):
    a = int(input("\nEnter value of a: \t"))
    b = int(input("Enter value of b: \t"))
    c = int(input("Enter value of c: \t"))

    x1=(-b - cmath.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b + cmath.sqrt(b**2-4*a*c))/(2*a)

    print ("The solutions to your quadratic equation is: \n", "X1 = ", x1, "\nX2 = ",x2)
    round += 1
    if round != prompt:
        print ("Solving next equation in a few...")
        time.sleep(3)
    else:
        pass

time.sleep(1)     
print("Thank you for using the quadratic equation solver!")
   
    






