#Guess my number app
import random
print("Welcome to the guess my number app.")
name = input("Enter name:\n")
print("I'm thinking of a number between 1 and 20.\n")
#generating random integers
x = random.randint(1,20)

#Gives user 5 tries.
for i in range(5):
    guess = int(input("Guess my number:\n")) 
    if guess > x:
        print("Too high!!!")    
    elif guess < x:
        print("Too low!!!") 
    else:    
        break 

#Check for whether user won or not
if guess == x:
    print("You are correct. You got the right answer after", i+1,"guesses.")
else:    
    print("Game over. The number was", x, ".You did not get the number after the available 5 tries.")