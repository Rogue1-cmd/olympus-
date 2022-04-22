#Epidemic Outbreak Terminal
import random

class Simulation:
    def __init__(self):
        self.day_number = 1

        print("\n I will need the size of population")
        self.population_size = int(input("\nEnter population size: "))

        print("\n Initially infected percentage of the population")
        self.infection_percent = int(input("\nEnter population size intially infected: "))/100

        print("\nI will need the probability that an individual may get infected: ")
        self.infection_probability = int(input("\nEnter infection probability: "))

        print("\nI will need information about how long the infection will last")
        self.infection_duration = int(input("\nEnter how long the infection lasts (in days): "))

        print("\nI will need the mortality rate of the infection.")
        self.mortality_rate = float(input("\nEnter the mortality rate of the infection: "))

        print("\nThe simulation can only run for a specified period of time")
        self.sim_days = int(input("\nEnter how long you would like the simulation to run: "))



             
class Person:
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, sim):
        self.infection_chance = random.randint(0, 100)
        if self.infection_chance < self.infection_probability:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True

    def update(self, sim):
        if self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                x = random.randint(0,100)
                if x < self.mortality_rate:
                    self.die()
                elif self.is_dead = False:
                    if self.days_infected = self.infection_duration:
                        self.heal()

        

class Population:
    def __init__(self, sim):
        self.population = []
        for person in range(self.population_size):
            person = Person(self)
            self.population.append(person)

    def initial_infection(self, sim):
        self.infected_count = int(round((self.infection_percent * self.population_size), 0))
        for i in range(self.infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1
            random.shuffle(self.population)
            

        
