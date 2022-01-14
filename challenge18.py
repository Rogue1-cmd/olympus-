#Voter registration app

print("Welcome to the voter registration app\n")
name = input("Enter your name:\n").title().strip()
age = int(input("Enter your age:\n"))
parties = ['ODM','KANU','Jubilee','OKA','UDA','ANC']

#Requesting user's age
if age >= 18:
    print(name,"You are an eligible voter. Please select a party from the list below")
    #display list of parties
    for party in parties:
        print("\t-",party)
    choice = input("Party chosen: \n")
    if choice in parties:
        print("Congratulations",name,",you are now a member of", choice,". Happy purging." )
    else:
        print("Sorry the party chosen does not exist")
#user not eligible voter
else:
    print ("Sorry",name,",you are not an eligible voter. Come back when you are 18.") 

#ToDo : make case insensitive               

