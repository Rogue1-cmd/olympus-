#grocery shopping list
import time
import datetime
import json

from difflib import get_close_matches

shopping_list = ["cheese", "meat"]
print("welcome to the shopping list app")

time = datetime.datetime.now()
mm = str(time.month)
dd = str(time.day)
hh = str(time.hour)
mn = str(time.minute)

print (mm,"/",dd," ", hh,":",mn)

print ("Your shopping list already contains", shopping_list[0], "and", shopping_list[1])

#adding items to shopping list
while True:
    items_ = input("Enter grocery items you wish to buy; \n")
    x = len(shopping_list)
    if x == 5:
        break
    else:
        shopping_list.append(items_) 

shopping_list.sort()        
print("Your shopping list", shopping_list)

#shopping
    
purchased = input ("Enter item purchased: \n")
shopping_list.remove(purchased)
print("Removing ", purchased, " from the list...")

purchased = input ("Enter item purchased: \n")
shopping_list.remove(purchased)
print("Removing ", purchased, " from the list...")

purchased = input ("Enter item purchased: \n")
shopping_list.remove(purchased)
print("Removing ", purchased, " from the list...\n")

print("Your shopping list is \n", shopping_list)

#items not in store
nis = shopping_list.pop()
print ("Sorry the store is out of",nis,":( \n")

prompt = input("What would you like to replace it with \n")
shopping_list.append(prompt)

print(shopping_list)



    




















    
    


