#Yes/No polling app
import time
print("Welcome to the Yes/No polling app.")
issue = input("Enter issue to vote on: \n").title()
no_of_voters = int(input("How many voters will be participating? : "))
password = input("Enter password you will use to access vote results : ")

yes_votes = 0
no_votes = 0
results = {}

print("\nVoting has started.")

for i in range(no_of_voters):
    name = input("\n\nEnter full name : ").title()
    if name in results.keys():
        print("\nYou have already votes bruh")
        time.sleep(1)
        print("shame!!!")
    else:
        time.sleep(1)
        print("\n",issue)    
        choice = input("\nDo you vote Yes/No: ").title().strip()
        if choice.startswith("Y"):
            yes_votes += 1
        elif choice.startswith("N"):
            no_votes += 1
        else :
            print("Invalid choice!! \nYour choice has been recorded but it will not count.")    
        
        #adding results to dictionary 
        results[name] = choice
        print("Thank you for voting.")

#print no of voters
print("\n\nSummary: \n The total number of voters was: ", no_of_voters) 

print("Names: \n")
for key in results.keys():
    print("\t-", key) 

#poll results
print("\n\nPoll: ",issue,"?")
time.sleep(1)
if yes_votes > no_votes:
    print("Yes wins!")
elif no_votes > yes_votes:
    print("No wins!")
else :
    print("It was a tie!")  

print("No: ", no_votes, "\t\tYes: ", yes_votes)


#full results
kufuli = input("\n\nEnter password to access full results: ")
if kufuli == password:
    for key, value in results.items():
        print("Name :", key,"\t"," Vote : ",value)
else :
    print("Wrong password!!!") 

time.sleep(2)               
print("\nOkay, we're done... You welcome.")




