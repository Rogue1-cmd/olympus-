#Pythonagachi Simulator
import random
import time

class Creature:
    def __init__ (self, name):
        self.name = name.title()

        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0

        self.food = 2
        self.is_sleeping = False
        self.is_alive = True
      

    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.hunger -= (random.randint(1, 4))
            print(self.name," ate a great meal")
        else:
            print(self.name," has no food. forage.")
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        x = random.randint(0, 2)
        print("\n",self.name, " wants to play a game")
        print(self.name, " is thinking of a number 0,1 or 2...")
        guess = int(input("Guess the number :\t"))
        time.sleep(2)
        if guess == x :
            print("You are correct")
            self.boredom -= 3
        else:
            print("You are incorrect")
            self.boredom -= 1

        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True
        self.tiredness -= 3
        self.boredom -= 1
        print(name," is sleeping")
        if self.tiredness < 0:
            self.tiredness = 0
        if self.boredom < 0:
            self.boredom = 0

    def awake(self):
        y = random.randint(0, 2)           
        if y == 0 :
            print(self.name, " just woke up.")
            self.is_sleeping = False
            self.boredom = 0
        else:
            print(self.name," won't wake up.")    
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print(self.name," took a bath.")

    def forage(self):
        food_found = random.randint(0, 4)
        self.food += food_found
        print("Food found :", food_found)

    def show_values(self):
        print(" name :\t ", self.name, "\n", "hunger :\t ",self.hunger, "\n", "boredom :\t ", self.boredom, "\n", "tiredness :\t ", self.tiredness,\
             "\n", "dirtiness :\t ", self.dirtiness, "\n", "food inventory :  ", self.food, "\n")
        if self.is_sleeping:
            print("Status: Sleeping")
        else:
            print("Status: Awake")    
         
    def increment_values(self, stage):
        self.hunger += random.randint(0, stage)         
        if self.is_sleeping == False :
            self.boredom += random.randint(0, stage)
            self.tiredness += random.randint(0, stage)
        self.dirtiness += random.randint(0, stage)

    def kill(self):
        if self.hunger >= 10:
            print(name, " starved to death.")
            self.is_alive = False

        elif self.dirtiness >= 10:
            print(name, " got an infection and died.")    
            self.is_alive = False

        elif self.boredom >= 10:
            self.boredom = 10
            print(name, " is bored and sleeping.")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 0
            print(name," is tired and sleepy.")    
            self.is_sleeping = True

#Defining Functions
def show_menu(Creature):            
    if  Creature.is_sleeping == True:
        choice = int(input("Press 6 :\t"))
        choice = "6"        
    else:
        choice = int(input("\nEnter 1 to Eat\n Enter 2 to Play\n Enter 3 to Sleep\n Enter 4 to bathe\n Enter 5 to Forage\n\t Enter choice: "))
    return str(choice)                             


def call_action(Creature, choice):
    if choice == "1":
        Creature.eat()
    elif choice == "2":
        Creature.play()    
    elif choice == "3":
        Creature.sleep()    
    elif choice == "4":
        Creature.clean()
    elif choice == "5":
        Creature.forage() 
    elif choice == "6":
        Creature.awake()       
    else:
        print("Invalid choice!!!")    

#main code
print("\n\tWelcome to the Pythonagachi Simulator.\n")
difficulty = int(input("\nEnter difficulty level(1-5):\t"))
if difficulty > 5:
    difficulty = 5
elif difficulty < 1:
    difficulty = 1

alive = True
while alive:
    name = input("Enter creature's name:\t")
    player = Creature(name)
    rounds = 1

    while player.is_alive:
            print("\n\tRound : ", rounds, "\n")
            player.show_values()
            round_move = show_menu(player)
            call_action(player, round_move)

            print("\n\tRound Summary:")
            player.show_values()
            prompt = input("\nPress Enter to continue: ")
            time.sleep(1)

            player.increment_values(difficulty)
            player.kill()
            rounds += 1
    time.sleep(2)
    print("R.I.P", player.name)    
    print(player.name," lived through ", rounds," rounds")
    prompt2 = input("\nWould you like to play again (y/n): ").lower()
    if prompt2 != "y":
        print("\nThank you for playing.")
        alive = False
    

   