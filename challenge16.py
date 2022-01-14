#Shipping Accounts Program
import time
names = ['Nic', 'Sue', 'Al', 'Rita', 'Sly']
print("Welcome to the shipping accounts program")
usr = input("Enter your name: \n").title()

if usr in names:
    print("Welcome",usr,".\n")
    print("The shipping costs are as follows\n")
    print("Shipping orders 0 to 100: $5.10 each\nShipping orders 100 to 500: $5.00 each\nShipping orders 500 to 1000: $4.95 each\nShipping orders over 1000: $4.80 each ")
    quantity = int(input("\nHow many items would you like to ship:\n"))
    if quantity <= 100:
        cost = 5.10*quantity
        cost = round(cost,2)
        print("The cost of shipping is $",cost)     
    elif quantity <= 500:
        cost = 5.00*quantity
        cost = round(cost,2)
        print("The cost of shipping is $",cost)        
    elif quantity <= 1000:
        cost = 4.95*quantity
        cost = round(cost,2)
        print("The cost of shipping is $",cost)        
    else:
        cost = 4.80*quantity
        cost = round(cost,2)
        print("The cost of shipping is $",cost)
    prompt = input("Would you like to place this order?:(y/n)\n")
    if prompt == 'y':
        print("Placing your order...")
        time.sleep(2)
        print("Done!!!. Thank You:)")
    elif prompt == "n":
        print("No order placed at this time.") 
    else:
        print("Invalid selection.")
       
else:
    print("Sorry you do not have an account with us.")
    time.sleep(1)
    prompt2 = input("Would you like to create an account(y/n):\n")  
    if prompt2 == 'y':
        new_usr = input("Enter your name; \n")
        names.append(new_usr)
        print("Account created. Try again.")
    else:
        print("Thank you. Goodbye")       










