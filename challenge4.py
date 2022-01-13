#program to calculate hypotenuse and area of right angle triangle
import math
from math import sqrt
print ("Welcome, I'll be helping you calculate hypotenuse and area of right angle triangle")
a = float (input ("Enter base: "))
b = float (input ("Enter height: "))

c_squared = a*a+b*b
c = sqrt(c_squared)

area = 0.5*a*b

c = round(c, 3)
area = round(area, 3)

print ("The hyptenuse is", c,"cm")
print ("The area of the triangle is", area)



