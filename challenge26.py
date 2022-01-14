#Factor generator app
import time
print("Welcome to the factor generator app")
flag = True


while flag:
    x = int(input("Enter number to find factors for: \t"))
    factors = []
    for i in range(1, x+1):
        if (x%i) == 0:
            factors.append(i)

    print("The factors of " ,x, "are:")
    for factor in factors:
        print(factor)

    time.sleep(2) 

    print ("\nIn Summary: \n")
    for i in range(int(len(factors)/2)):
        print (factors[i],"*",factors[-i-1], "=", (x))  

    time.sleep(2)

    prompt = input("Would you like to try again ?(y/n): \n").lower()
    if prompt != "y":
        flag = False
        print("Okay bye")



