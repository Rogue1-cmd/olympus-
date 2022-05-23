#Epidemic Outbreak GUI
import tkinter
import time
import math
import random

#CLASSES
class Simulation:
    def __init__(self):
        self.day_number = 1
        self.population_size = int(input("Enter Population Size: "))
        #Make sure population size a perfect square
        root = math.sqrt(self.population_size)

        if int(root+0.5)**2 != self.population_size:
            root = round(root, 0)
            self.grid_size = int(root)
            population_size = (self.grid_size**2)
            print("\n\tPopulation size has been rounded to,", population_size, "\n\tfor visual purposes.")
        else:
            self.grid_size = int(math.sqrt(self.population_size))

        self.infection_percent = int(input("\nEnter population size initially infected: "))/100

        self.infection_probability = float(input("\nEnter probability of getting infected: "))

        self.infection_duration = int(input("\nHow long does the infection last: "))

        self.mortality_rate = float(input("\nEnter mortality rate of infection: "))

        self.sim_days = int(input("\nHow long should the simulation run: ")) 



class Person:
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, sim):
        self.infection_chance = random.randint(0, 100)
        if self.infection_chance > sim.infection_probability:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True

    def update(self, sim):
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                x = random.randint(0, 100)
                if x < sim.mortality_rate:                    
                    self.die()
                elif self.is_dead == False:
                    if self.days_infected == sim.infection_duration:
                        self.heal()
         


class Population:
    def __init__(self, sim):
        self.population = []# Holds all individuals
        for i in range (sim.grid_size):
            #Create grid_size number of rows 
            row = []
            for j in range(sim.grid_size):

                #create a person object
                person = Person()
                row.append(person)
            #Append row to population list
            self.population.append(row)

    def initial_infection(self, sim): #infect the correct starting amount
        infected_count = int(round(sim.infection_percent * sim.population_size, 0))
        infections = 0
        while infections < infected_count:
            x = random.randint(0, sim.grid_size -1)
            y = random.randint(0, sim.grid_size -1)

            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1

    def spread_infection(self, sim):

        #loop through the rows
        for i in range(sim.grid_size):

            #Loop through the objects
            for j in range(sim.grid_size):
                #If person is alive and adjacent person is infected, the person will be infected too 
                if self.population[i][j].is_dead == False:
                    if i == 0 : #First person on row, cannot check above rows (none)
                        if j == 0: #First person in first row, cannot check left
                            if self.population[i][j+1].is_infected ==True or self.population[i+1][j] == True: #right and below
                                self.population[i][j].infect(sim)

                        elif j == (sim.grid_size-1): #Last person in the first row, cannot check right
                            if self.population[i][j-1].is_infected == True or self.population[i+1][j].is_infected == True:
                                self.population[i][j].infect(sim)

                        else:         #can check left, right and below
                            if self.population[i][j+1].is_infected == True or self.population[i][j-1].is_infected == True or self.population[i+1][j].is_infected == True:
                                self.population[i][j].infect(sim)


                    elif i == (sim.grid_size -1): #Last row, cannot check rows below

                        if j == 0: #First person in the last row, cannot check left
                            if self.population[i][j+1].is_infected == True or self.population[i-1][j] == True:
                                self.population[i][j].infect(sim)


                        elif j == (sim.grid_size - 1): #Last person in the last row, cannot check right
                            if self.population[i][j-1].is_infected == True or self.population[i-1][j] == True:
                                self.population[i][j].infect(sim)

                        else:    #can check right, left and above
                            if self.population[i][j-1].is_infected == True or self.population[i][j+1].is_infected == True or self.population[i-1][j].is_infected == True:
                                self.population[i][j].infect(sim)


                    else:
                        # i represents rows in the middle
                        #can check right, left, above and below
                        if j == 0: # First person in a row, cannot check left
                            if self.population[i][j+1].is_infected == True or self.population[i-1][j].is_infected == True or self.population[i+1][j].is_infected == True:
                                self.population[i][j].infect(sim)

                        elif j == (sim.grid_size -1):         # Last person in row, cannot check right
                            if self.population[i][j-1].is_infected == True or self.population[i-1][j].is_infected == True or self.population[i+1][j].is_infected == True:
                                self.population[i][j].infect(sim)

                        else:     #can check right, left, above, below
                                if self.population[i][j+1].is_infected == True or self.population[i][j-1].is_infected == True or self.population[i-1][j].is_infected == True or self.population[i+1][j].is_infected == True:
                                    self.population[i][j].infect(sim)
    

    def update(self, sim):
        sim.day_number += 1

        for row in self.population:
            for person in row:
                person.update(sim)

    def display_statistics(self, sim):
        total_infected_count = 0
        total_death_count = 0

        #loop through population>> Loop through row


        for row in self.population:

            for person in row:
            
                if person.is_infected: #Infected
                    total_infected_count += 1
                    if person.is_dead:#Dead
                        total_death_count += 1 


        infected_percent = round((total_infected_count / sim.population_size)*100, 4)
        death_percent = round((total_death_count/ sim.population_size)*100, 4)


        print("\n\t -----------SUMMARY------------\n")
        print("\tpopulation : ", sim.population_size)
        print("\n\tDay number : ",sim.day_number)           
        print("\n\tInfected : ", total_infected_count)
        print("\n\tDead : ", total_death_count)
        print("\n\tPercent Infected :", infected_percent)
        print("\n\tPercent Dead :", death_percent)


#FUNCTIONS       
def graphics (sim, populus, canvas):
    square_dimension = 600 // sim.grid_size
    for i in range(sim.grid_size) :
        y = i*square_dimension #Index of square
        for j in range(sim.grid_size):
            x = j * square_dimension #Index of square
            if populus.population[i][j].is_dead:
                canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill= "red")
            else:
                if populus.population[i][j].is_infected == True:
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill= "yellow")
                else:
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill= "green")


#Maincode

sim = Simulation()

#window size
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

#canvas
sim_window = tkinter.Tk()
sim_window.title("Outbreak Now")
sim_canvas = tkinter.Canvas(sim_window, width= WINDOW_WIDTH, height= WINDOW_HEIGHT, bg= "white")
sim_canvas.pack(side= tkinter.LEFT)

populus = Population(sim)
populus.initial_infection(sim)
populus.display_statistics(sim)

prompt = input("Press enter to begin simulation...")
time.sleep(2)

for i in range(sim.sim_days):
    populus.spread_infection(sim)
    populus.update(sim)
    populus.display_statistics(sim)

    graphics(sim, populus, sim_canvas)

    sim_window.update() #Update tkinter to new graphics
    time.sleep(3)

    if i != sim.sim_days - 1: #Clear canvas if not in the last day of simulation
        time.sleep(5)
        sim_canvas.delete("all")

































                















        
