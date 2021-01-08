import random
import math
from Individual import Individual

class Population:

    def __init__(self, population_size, genes_quantity):
        self.populationList = []
        self.populationFitness = 0
        for each in range(0, population_size):
            self.populationList.append(Individual(genes_quantity))

    def get_population_fitness(self):
        temp_fitness = 0
        for individual in self.populationList:
            temp_fitness += individual.get_fitness()
        return temp_fitness

    def print_population(self):
        # Print each individual of the population
        print("The population: ")
        for individual in self.populationList:
            individual.print_info()

    # Tournament
    def tournament_population(self):
        temp_population = []
        for each in range(0, len(self.populationList)):
            # pick two random individuals
            child1 = random.choice(self.populationList)
            child2 = random.choice(self.populationList)

            if child1.get_fitness() < child2.get_fitness():
                temp_population.append(child1)
            else:
                temp_population.append(child2)
        self.populationList = temp_population

    # Crossover
    def crossover_population(self):
        for individual in self.populationList:
            random_partner = random.choice(self.populationList)
            individual.crossover(random_partner)

    # Mutation
    def mutate_population(self, mutation_rate, mutation_magnitude_max):
        for individual in self.populationList:
            individual.mutate_genes(mutation_rate, mutation_magnitude_max)
