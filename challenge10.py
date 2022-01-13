#Favourite teachers program
import time
print("Hey, Welcome")
fav_teachers = []

#prompt user to enter teachers names
while True :
    
    if len(fav_teachers) == 4:
        break        
    else:
        prompt = input("Enter the name of your favourite teacher: \n").title()
        fav_teachers.append(prompt)
        
print("Your four favourite teachers ranked are:\n",str(fav_teachers)) 
print("Your four favourite teachers ranked alphabetically are:\n",str(sorted(fav_teachers)))
print("Your four favourite teachers ranked in reverse alphabet are:\n",str(sorted(fav_teachers, reverse= True )))
print("Your top two favourite teachers are:\n",str(fav_teachers[0:2]))
print("Your last two favourite teachers are:\n",str(fav_teachers[2:]))
print("Your last favourite teachers are:\n",str(fav_teachers[3]))
print("Your have", len(fav_teachers), "favourite teachers")
"\n"

time.sleep(1) #stop execution for a second
print("You no longer like one teacher")
prompt2 = input ("Pick teacher to remove:\n").title()
print ("removing", prompt2)

fav_teachers.remove(prompt2)

print("Your four favourite teachers ranked are:\n",str(fav_teachers)) 
print("Your four favourite teachers ranked alphabetically are:\n",str(sorted(fav_teachers)))
print("Your four favourite teachers ranked in reverse alphabet are:\n",str(sorted(fav_teachers, reverse= True )))
print("Your top two favourite teachers are:\n",str(fav_teachers[0:2]))
print("Your last two favourite teachers are:\n",str(" and ".join(fav_teachers[1:])))
print("Your last favourite teachers are:\n",str(fav_teachers[2]))
print("Your have", len(fav_teachers), "favourite teachers")






