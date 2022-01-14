#Fibonacci Calculator 
print("Welcome to the Fibonacci Calculator App")
n = int(input ("Enter no of digits you'd like\n"))
seq =[1,1]

#Fibonacci algorithm using for loop
for i in range(n-2): #assign object items to target
    y = seq[i]+seq[i+1]
    seq.append(y)
print("The first",n, "terms of The Fibonacci sequence are; \n", seq)

#Finding the golden ration -phi
ratio = []
for i in range(n-2):
    x = seq[i+1]/seq[i]
    ratio.append(x)
print("The corresponding golden ratio values are\n", ratio)   

#using the zip() function
print("Heres a tabular format\n")
for a,b in zip(seq, ratio):
    print(a,"-----",b,"-----")

print("The golden ratio approaches an irrational value 1.618")