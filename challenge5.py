#A program for multiplication table and exponentials of given number
name = input ("What's your name? \n")
number = float (input ("Enter number: \n"))
message = name.title()+", Math is cool, right!?\n"
print (message, "The multiplication table for", number, "is")

print (round(number*1,3),"=", number, "*1")
print (round(number*2,3),"=", number, "*2")
print (round(number*3,3),"=", number, "*3")
print (round(number*4,3),"=", number, "*4")
print (round(number*5,3),"=", number, "*5")
print (round(number*6,3),"=", number, "*6")
print (round(number*7,3),"=", number, "*7")
print (round(number*8,3),"=", number, "*8")
print (round(number*9,3),"=", number, "*9")


print ("\nThe exponential table for", number, "is")

print (round(number**1,3),"=", number, "**1")
print (round(number**2,3),"=", number, "**2")
print (round(number**3,3),"=", number, "**3")
print (round(number**4,3),"=", number, "**4")
print (round(number**5,3),"=", number, "**5")
print (round(number**6,3),"=", number, "**6")
print (round(number**7,3),"=", number, "**7")
print (round(number**8,3),"=", number, "**8")
print (round(number**9,3),"=", number, "**9")

