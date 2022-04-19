#Pykemon Simulator
import random
import time

class Pykemon:#Parent
    def __init__(self, name, element, health, speed):
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        damage = random.randint(15, 25)
        print(self.name, "used", self.moves[0], " on the enemy pykemon")
        print("Damage: ", damage)
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        damage = random.randint(0, 50)
        print(self.name, "used", self.moves[1], " on the enemy pykemon")

        if damage < 10 :
            print("Attack missed.")
        else:
            print("Damage Inflicted: ", damage)
            enemy.current_health -= damage

    def restore(self): #Restores current health
        heal = random.randint(15, 25)
        print(self.name, "used", self.moves[2])
        print("Pykemon has been healed by, ", heal, "points.")
        self.current_health += heal
        if self.current_health > self.max_health: #in case max health was exceeded
            self.current_health = self.max_health

    def faint(self):
        if self.current_health <= 0:
            self.is_alive = False
            print(self.name, "has fainted.")
            input("Press enter to continue.")

    def show_stats(self):
        print("\n\t Name:", self.name,"\n\tElement:", self.element, "\n\tCurrent Health:",\
             self.current_health, "\n\tMax Health:", self.max_health, "\n\tSpeed:", self.speed,)
            


class Fire(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Scratch", "Ember", "Light", "Fire Blast"]

    def special_attack(self, enemy): #massive damage to grass; normal to fire; and minimal water type Pykemon
        print(self.name, "has used ",self.moves[3])

        if enemy.element == "GRASS":
            print("\nAttack was super effective.")
            damage = random.randint(35, 50)
        elif enemy.element == "WATER":
            print("\nAttack was not very effective.")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print("Damage inflicted: ",damage)
        enemy.current_health -= damage

    def move_info(self):
        print("\t-----",self.name, "Moves-----")

        print("\nScratch:\n\t-- 15 to 25 damage points (Efficient attack.)",\
             "\nEmber:\n\t-- 0 to 50 damage points (Risky attack.)",\
             "\nLight:\n\t-- Heal your Pykemon 15 to 25 health points (Restorative)",\
             "\nFire Blast:\n\t-- MASSIVE damage to GRASS type Pykemon (powerful FIRE based attack...)")  




class Water(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Bite", "Splash", "Dive", "Water Cannon"]

    def special_attack(self, enemy):
        print(self.name, "used ", self.moves[3])
        if enemy.element == "Fire":
            print("Attack was super effective.")
            damage = random.randint(35, 50)
        
        elif enemy.element == "grass":
            print("move was not very effective")
            damage = random.randint(5, 10)
        
        else :
            damage = random.randint(10, 20)

        print("Damage inflicted: ",damage)
        enemy.current_health -= damage

    def move_info(self):
        print("\t-----", self.name, "Moves-----")
        print("\nBite:\n\t-- 15 to 25 damage points (Efficient attack.)",\
             "\nSplash:\n\t-- 0 to 50 damage points (Risky attack.)",\
             "\nDive:\n\t-- Heal your Pykemon withs 15 to 25 health points (Restorative)",\
             "\nWater Cannon:\n\t-- MASSIVE damage to Fire type Pykemon (powerful water based attack...)")  
                    


class Grass(Pykemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]

    def special_attack(self, enemy):
        print(self.name, "used ",self.moves[3])

        if enemy.element == "WATER":
            print("Attack was super effective.")
            damage = random.randint(35, 50)

        elif enemy.element == "FIRE":
            print ("Attack was not effective.")
            damage = random.randint(5, 10)

        else:
            damage = random.randint(10, 30)
        
        print("Damage = ", damage)
        self.current_health -= damage

    def move_info(self):
        print("\t-----", self.name, "Moves-----")
        print("\nVine Whip:\n\t-- 15 to 25 damage points (Efficient attack.)",\
             "\nWrap:\n\t-- 0 to 50 damage points (Risky attack.)",\
             "\nGrow:\n\t-- Heal your Pykemon withs 15 to 25 health points (Restorative)",\
             "\nLeaf Blade:\n\t-- MASSIVE damage to Water type Pykemon (powerful Grass based attack...)")

             
        
class Game():
    def __init__(self):
        self.pykemon_elements = ["FIRE", "WATER","GRASS"]
        self.pykemon_names = ["Chewdie", "Spatol", "Burnmander", "Pykachu", "Pyonx",\
             "Abbacab", "Sweetil", "Jampot","Hownstooth", "Swagilybo", "Muttle",\
             "Zantbat", "Wiggly Poof", "Rubblesaur"]
        self.battles_won = 0 #Tracks how many pykemons have been defeated.

    def create_pykemon(self):
        health = random.randint(70, 100)
        speed = random.randint(1, 10)
        element = random.choice(self.pykemon_elements)
        name = random.choice(self.pykemon_names)

        if element == "FIRE":
            pykemon = Fire(name, element, health, speed)

        elif element == "WATER":
            pykemon = Water(name, element, health, speed)

        else :
            pykemon = Grass(name, element, health, speed)

        return pykemon

    def choose_pykemon(self):
        starters = [] #Holds three unique pykemon
        while len(starters) < 3:
            pykemon = self.create_pykemon() #Makes starter pykemon

            valid_pykemon = True            
                #loop through the starters list and check if the starter name and element are \
                # and element are equal to the currently created Pykemon's name and element. 
            for starter in starters:
                if starter.name == pykemon.name or starter.element == pykemon.element:
                    valid_pykemon = False #deactivate flag if similar

            if valid_pykemon: #Pykemon has not been created
                starters.append(pykemon) #Append new pykemon to list

        for starter in starters:
            starter.show_stats()
            starter.move_info()

        print("\nThe professor presents you with 3 Pykemons")
        print("\nPress \n\t1.", starters[0].name ,"\n\t2.", starters[1].name , "\n\t3.", starters[2].name)
        choice = int(input("\n\tChoose one : "))                

        if choice == 1:
            pykemon = self.starters[0]
        elif choice == 2:
            pykemon = self.starters[1]
        else :
            choice == 3
            pykemon = self.starters[2]

        return pykemon

    def get_attack(self, pykemon):
        print("What move would you like to play?")
        print("Press \n\t1.", pykemon.moves[0], "\n\t2.",\
             pykemon.moves[1], "\n\t3.", \
             pykemon.moves[2], "\n\t4.", \
             pykemon.moves[3])

        move = int(input("Enter move choice: "))
        print("\n")
        print("------------------------------------")
        return move

    def player_attack(self, move, player, computer):
        if move == 1:
            player.light_attack(computer) 
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        else :
            move == 4
            player.special_attack(computer)
        computer.faint()

    def computer_attack(self, player, computer):
        move = random.randint(1,4)
        if move == 1:
            computer.light_attack(player) 
        elif self.move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        else :
            move == 4
            computer.special_attack(player)
        player.faint()


    def battle(self, player, computer):

        move = self.get_attack(player)

        if player.speed >= computer.speed: #Player Attacks
            self.player_attack(move, player, computer)

            if computer.is_alive: #Computer attacks
                self.computer_attack(player, computer)

        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)

        
#Main Code
print("\t-------Welcome to the Pykemon Simulator------.\
      \n---Prof Pete is gonna give you your first Pykemon--- \
      \n\n----There are three options to choose from---\n")

input("Press Enter to Continue")

time.sleep(3)

playing_main = True
while playing_main:
    game = Game()

    player = game.choose_pykemon() #Choose pykemon
    print("\nPykemon selected: ",player.name)

    player.show_stats()

    while player.is_alive:
        computer = game.create_pykemon() #Creates computer pykemon to battle
        print("\nDANGER!!! DANGER!!! a wild", computer.name, "approaches.")
        computer.show_stats()
        
        while player.is_alive and computer.is_alive:
            game.battle(player, computer)

            #Both survived
            if player.is_alive and computer.is_alive :
                player.show_stats()
                computer.show_stats()
                print("----------------------------")

        if player.is_alive:
            game.battles_won += 1

    print(Pykemon.self.name, "has fainted.")
    print("Your pykemon defeated", game.battles_won)

    prompt2 = int(input("Would you like to try again? (y/n)")).lower()
    if prompt2 != "y":
        playing_main = False
        print("\nThank you for playing.")
        






            



                        




        

