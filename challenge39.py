#Epidemic Outbreak Terminal
import random
import time
import colorama
from colorama import Fore

class Simulation:
    def __init__(self):
        self.day_number = 1

        print("\n       I will need the size of population")
        self.population_size = int(input("\nEnter population size: "))
        print("\n")

        print("\n       Initially infected percentage of the population")
        self.infection_percent = int(input("\nEnter population size intially infected: "))/100
        print("\n")

        print("\n       I will need the probability that an individual may get infected: ")
        self.infection_probability = float(input("\nEnter infection probability: "))
        print("\n")

        print("\n       I will need information about how long the infection will last")
        self.infection_duration = int(input("\nEnter how long the infection lasts (in days): "))
        print("\n")

        print("\n       I will need the mortality rate of the infection.")
        self.mortality_rate = float(input("\nEnter the mortality rate of the infection: "))
        print("\n")

        print("\n       The simulation can only run for a specified period of time")
        self.sim_days = int(input("\nEnter how long you would like the simulation to run: "))
        print("\n")



             
class Person:
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, sim):
        self.infection_chance = random.randint(0, 100)
        if self.infection_chance < sim.infection_probability:
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
                x = random.randint(0,100)
                if x < sim.mortality_rate:
                    self.die()
                elif self.is_dead == False:
                    if self.days_infected == sim.infection_duration:
                        self.heal()

        

class Population:
    def __init__(self, sim):
        self.population = []

        for person in range(sim.population_size):
            person = Person()
            self.population.append(person)

    def initial_infection(self, sim):
        infected_count = int(round((sim.infection_percent * sim.population_size), 0))

        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1

        random.shuffle(self.population)

    def spread_infection(self, sim):
        for i in range(len(self.population)):

            if self.population[i].is_dead == False: 

                if i == 0: #First person on the list
                    #check to see if person on the right is infected
                    if self.population[i+1].is_infected == True:
                        self.population[i].infect(sim)
                
                elif i < (len(self.population) - 1): #persons in the middle of the lists
                    #check to see if person on either side is infected.
                    if self.population[i+1].is_infected == True or self.population[i-1].is_infected == True:
                        self.population[i].infect(sim)
                
                elif i == (len(self.population)-1): #Last person on the list
                    #check if second last person is infected
                    if self.population[i-1].is_infected == True:
                        self.population[i].infect(sim)

    def update(self, sim):
        sim.day_number += 1
        for i in self.population:
            i.update(sim)

    def display_statistics(self, sim):
        total_infected_count = 0
        total_dead_count = 0

        for i in self.population:
            
            if i.is_infected:
                total_infected_count += 1
                if i.is_dead:
                    total_dead_count += 1

        infected_percent = round(((total_infected_count/sim.population_size)*100), 4)

        death_percent = round(((total_dead_count/sim.population_size)*100), 4)

        print(Fore.WHITE+ "\n\t--------Statistics Summary--------")
        print(Fore.BLUE+"\n\tDay : ", sim.day_number)
        print(Fore.BLUE+"\n\tPopulation : ", sim.population_size)
        print(Fore.BLUE+"\n\tPercent Infected: ", infected_percent, "%")
        print(Fore.BLUE+"\n\tPercent Dead: ", death_percent, "%")
        print(Fore.BLUE+"\n\tTotal Infected: ", total_infected_count)
        print(Fore.BLUE+"\n\tTotal Dead: ", total_dead_count)

    def graphics(self):
        status = []
        for i in self.population:
            if i.is_dead:
                char = "X"
            else:
                if i.is_infected:
                    char = "I"
                else:
                    char = "O"
            status.append(char)

        for i in status:
            print(Fore.MAGENTA+ i, end = " - ") 
            

        print("\nO : Healthy    ", "I : Infected    ", "X : Dead")


#Main code
print(Fore.LIGHTRED_EX + "Welcome to Epidemic Terminal")
time.sleep(0.5)
sim = Simulation()
population = Population(sim)

population.initial_infection(sim)
population.display_statistics(sim)
time.sleep(3)
population.graphics()

input("\nPress enter to begin simulation")

for i in range(1, sim.sim_days):
    population.spread_infection(sim)
    population.update(sim)
    population.display_statistics(sim)
    time.sleep(4)
    population.graphics()
    time.sleep(3)

    if i != sim.sim_days:
        prompt = input("\nPress enter to move to the next day of simulation.")
        








            




        
