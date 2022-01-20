#Python  Dice Roll
import random 

def dice_sides():
    sides = int(input("\nHow many sides of dice would you like? : "))
    return sides

def dice_number():
    number = int(input("\nHow many dice would you like to roll?: "))
    return number

def roll_dice(sides, number):
    dice = []
    print("\nYou rolled ", number, sides, "sided dice.")
    for i in range(number):
        roll = random.randint(1, sides)
        dice.append(roll)
    print("\t----------RESULTS----------")    
    for i in dice:
        print("\t\t -", i)    
    return dice     

def sum_dice(dice):
    x = sum(dice)
    print("\nThe total value of your roll is", x)

def roll_again():
    choice = input("\nWould you like to roll again? (y/n):").lower()
    if choice == "y":
        active = True
    else :
        active = False 
    return active        


print("\t\tWelcome to the python dice app.\n")
active = True
while active:
    x = dice_sides()    
    y = dice_number()
    
    rolled_dice = roll_dice(x, y)
    sum_dice(rolled_dice)

    active = roll_again()

print("\nThank you for playing. Bye.\n")

    

