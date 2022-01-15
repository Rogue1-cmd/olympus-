#Even & odd numbers sorter
import time # just to make it more appealing to user
print("Welcome to the even and odd numbers sorter app.")

active = True # setting flag

while active:
    usr_input = input("Enter list of numbers separated by commas: \t")
    usr_input = usr_input.replace(" ", "") 
    num_list = (usr_input.split(","))

    evens = []
    odds = []
    print("Working on it..."); time.sleep(2)

    print("\nSummary: \n")
    for number in num_list:
        number = int(number)
        if (number%2 == 0):
            evens.append(number)
            print(number, " is even"); time.sleep(0.5)
        else:
            odds.append(number)   
            print(number, "is odd"); time.sleep(0.5)

    evens.sort()      
    odds.sort()  
     
    time.sleep(2)

    print("\nThe following", len(evens),"numbers are even:\n"); time.sleep(0.5)
    for number in evens:
        print("\t -", number); time.sleep(0.5)

    print("\nThe following", len(odds),"numbers are odd:\n") ; time.sleep(0.5)
    for number in odds:
        print("\t -", number); time.sleep(0.5)

    prompt = input("Would you like to try again? (y/n): \t").lower()        
    if prompt != "y":
        active = False 
        print("Okay, bye.")
