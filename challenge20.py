#Rock paper scissors
import random
import time
print("Welcome to the rock paper scissors game.")
rounds = int(input("How many rounds would you like to play?\n"))

#Initializing variables
moves = ["Rock","Paper","Scissors"]
Player = 0
Computer = 0

for i in range(rounds):
    print ("\nRound", i+1, ":")
    print ("Player =", Player, "\tComputer =", Computer) #scores

    x = random.randint(0,2)
    com = (moves[x]) #computer's move
    ply = input("Lets go... Rock, Paper, Scissors: ").title() #player's move
    time.sleep(1)
    
    if ply in moves:
        print("\tComputer = ",com, "\n\tPlayer = ", ply)
        if (com == "Rock") and (ply == "Paper"):
            print ("Paper covers Rock")
            print ("Player wins!")
            Player += 1
        elif (com == "Rock") and (ply == "Scissors"):
            print ("Rock crushes Scissors")
            print ("Computer wins!")
            Computer += 1
        elif (com == "Paper") and (ply == "Scissors"):
            print ("Scissors cut Paper")
            print ("Player wins!")
            Player += 1
        elif (com == "Paper") and (ply == "Rock"):
            print ("Paper covers Rock")
            print ("Computer wins!")
            Computer += 1
        elif (com == "Scissors") and (ply == "Paper"):
            print ("Scissors cuts Paper") 
            print ("Computer wins!")   
            Computer += 1
        elif (com == "Scissors") and (ply == "Rock"):
            print ("Rock crushes Scissors")
            print ("Player wins!")
            Player += 1
        elif (com == ply):
            print ("Draw!!!")
    else:
        print("Invalid input") 
        print("Computer wins!")
        Computer += 1   

print("FINAL RESULTS :\n")
time.sleep(2)
print("Rounds :",rounds)
if Computer > Player:
    print ("\tPlayer =", Player, "\tComputer =", Computer)
    print("\tComputer wins!!")
elif Computer < Player:
    print ("\tPlayer =", Player, "\tComputer =", Computer)
    print("\tNICE...YOU WON!!")
else:
    print("\tDraw.")    


##to make user interface more easy on the eyes




