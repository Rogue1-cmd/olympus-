#Power Ball Simulator
import random


print ("\t\tWelcome to the Power-Ball.")

white_balls = int(input("\nHow many white balls will you choose from ?(normally 69): \t"))
if white_balls < 5:
    white_balls = 5

red_balls = int(input("How many red balls will you choose from ?(normally 26): \t"))
if red_balls < 1:
    red_balls = 1

odds = 1
for i in range(5):
    odds *= white_balls-i
odds *= red_balls/120    

print("\nThe odds of winning this lottery are 1 in ", odds,".\nMay the odds be in your favour;-)")

ticket_interval = int(input("\nHow may tickets would you like to purchase at each interval : \t"))

#creating the lotto numbers
winning_numbers = []
while len(winning_numbers) < 5:
    x = random.randint(1, white_balls) 
    if x not in winning_numbers:
         winning_numbers.append(x)
winning_numbers.sort()

y = random.randint(1, red_balls)
winning_numbers.append(y)

#Actual Power Ball draw
print("Welcome to the Power Ball Draw. The winning numbers are: ")
print("\t\t", end= "")
for number in winning_numbers:
    print(number, end= ' ')

input("\n\nPress enter to start purchasing tickets: ")

#initializing
tickets_purchased = 0
active = True
tickets_sold = []

#Will run as long as winning ticket has not been purchased and user hasn't given up
while winning_numbers not in tickets_sold and active == True :
    lottery_numbers = []
    while len(lottery_numbers) < 5:
        x = random.randint(1, white_balls) 
        if x not in lottery_numbers:
            lottery_numbers.append(x)            
    lottery_numbers.sort()

    x = random.randint(1, red_balls)
    lottery_numbers.append(x)

    if lottery_numbers not in tickets_sold:
        tickets_purchased += 1
        tickets_sold.append(lottery_numbers)
        print(lottery_numbers)
    else:
        print("Losing ticket was generated and disregarded.")

    if (tickets_purchased)%(ticket_interval)== 0:
        print("\nTotal number of tickets purchased so far : ", tickets_purchased,".\nNow winners yet!!!")
        choice = input("\nWould you like to purchase more tickets(y/n): ").lower()
        if choice != "y":
            active = False

if lottery_numbers == winning_numbers:
    print("\nYou won the lottery!!!\nThe winning number were : ", winning_numbers)            
    print("\nYou purchased", tickets_purchased," tickets.")
else:
    print("\n\nYou have purchased",tickets_purchased," tickets but haven't won yet.\nThe odds were not in your favour :-( ...\n\n")    








