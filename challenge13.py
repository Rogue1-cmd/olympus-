#Factorial Calculator App
import math 
import time

print("Welcome to the factorial calculator")
num = int(input ("Enter number: \n"))

print(num, "! =",end="")
for i in range(1, num):
    print(i, end="*")
print(num)


if type(num) != int: #for when input is not an integer (hasn"t worked yet)
    print("Invalid input")

print ("The input is of ",type(num), "type")

fact = 1
for i in range(1, num+1):
    fact = fact*i
print("The factorial of ", num, "from my algorithm is", fact)

time.sleep(2)
ans = math.factorial(num)  
print("The factorial of ",num, "from math library is", ans)  