#Bank deposit and withdrawal

#Customer details
def get_info():
    print ("\t\tWelcome to the Goliath National Bank.\n")
    info = {}
    info["Name"] = input("Enter name:\t")
    info["Balance_Savings"] = float(input("Enter Initial deposit to Savings account:\t"))
    info["Balance_Checking"] = float(input("Enter Initial deposit to Checking account:\t"))
    return info

#making a deposit
def make_deposit(info, acc_type, amnt):
    if acc_type == "1":
        info["Balance_Checking"] = info["Balance_Checking"] + amnt
        print("Confirmed.\n Deposited ",amnt, "shillings to Checking account.")

    elif acc_type == "2":
        info["Balance_Savings"] = info["Balance_Savings"] + amnt
        print("Confirmed.\n Deposited ",amnt, "shillings to Savings account.")

    else :
        print("Invalid Operation.")   
    return (" ")

#making a withdrawal
def make_withdrawal(info, acc_type, amnt):
    if acc_type == "1":
        if info["Balance_Checking"] > amnt:
            info ["Balance_Checking"] = info ["Balance_Checking"]-amnt
            print("\nYou have withdrawn",amnt, "shillings from your checking account.")
        else:
            print("No transaction has occured as you will have a negative balance")
    elif acc_type == "2":
        if info["Balance_Savings"] > amnt:
            info ["Balance_Savings"] = info ["Balance_Savings"]-amnt
            print("\nYou have withdrawn",amnt, "shillings from your savings account.")
        else:
            print("No transaction has occured as you will have a negative balance")
    else :
        print("Invalid Operation.") 
    return (" ")    

#displaying customer info
def display_info(info):
    print("\n      ACCOUNT INFO      ")
    for k, v in info.items():
        print("\n",k, ": ",v)
    return (" ")        

        

account = get_info()               
active = True
while active:
    account_info = display_info(account)
    print(account_info)
    
    acc_type = input("\nChoose account (Enter 1 or 2): \n\t1. Checking\n\t2. Savings\n\t")
    transaction  = input("\nChoose transaction(Enter 1 or 2): \n\t1. Deposit\n\t2. Withdrawal\n\t")
    amnt = float (input("\nHow much money will you be working with: \t"))
    if acc_type == "1" or "2":
        if transaction == "1":
            x = make_deposit(account, acc_type, amnt)
            print(x)
        elif transaction == "2":
            x = make_withdrawal(account, acc_type, amnt)
            print(x)
        else:
            print("\nApologies. Transaction cannot be completed.")    
    else :
        print("Transaction cannot be completed.")
    choice = input("\n\nWould you like to make another transaction(y/n):").lower()    
    if choice != "y":
        print ("\n\t\t----SUMMARY----")
        account_info = display_info(account)
        print(account_info)
        active = False














        








