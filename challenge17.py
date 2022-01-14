#Coin toss app
import random
print("Welcome to the coin toss app")
n = int(input("How many times would you like to toss your coin:\n"))
n2 = input("Would you like to see the result of each coin toss?:\n").lower()

h = 0
t = 0

for i in range(n):
    flip = random.randint(0,1)
    if (flip == 0):
        h += 1
        if n2.startswith('y'):
            print("H")
    else :
        t += 1
        if n2.startswith('y'):
            print("T")
    if h==t:
        print("The number of heads and tails were equal at the",i+1,"flip at", h,"each")

h_percentage = round(100*(h/n),2)  
t_percentage = round(100*(t/n),2)   

print("The results of flipping the coin",n,"times are :\n")
print("\nSide\t\tCount\t\tPercentage")
print("Heads\t\t",h, "/",n, "\t\t",h_percentage,"%")
print("Tails\t\t",t, "/",n, "\t\t",t_percentage,"%")

#using zip()... has not worked yet!!!!
for Heads, Tails in zip(h_percentage, t_percentage):
    print(Heads,"\t", Tails,"\t")





