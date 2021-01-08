# Simple genetic algorithm
import random
from Individual import Individual
import matplotlib.pyplot as plt
import numpy as np


# Tournament selection
def tournament(population):
    children = []
    for individual in population:
        # Grab two random individuals from the population
        child1 = random.choice(population)
        child2 = random.choice(population)

        if child1.get_fitness() < child2.get_fitness():
            children.append(child1)
        else:
            children.append(child2)
    return children


def crossover(population):
    temp_pop = []
    for i in range(0, len(population), 2):
        temp_pop.extend(population[i].crossover(random.choice(population)))

    return temp_pop


def get_population_fitness(population):
    temp_fitness = 0
    for individual in population:
        temp_fitness += individual.get_fitness()
    return temp_fitness


def main():
    # make a population list comprising of individuals with a 10long genome
    pop = []
    for _ in range(0, 50):
        pop.append(Individual(10))

    for i in pop: i.print_info()
    print("\n/////////////////////")

    avg_fitness = []
    for i in range(0, 50):
        # tournament
        pop = tournament(pop)
        # mutate
        for individual in pop: individual.mutate_genes
        # crossover
        #pop = crossover(pop)
        avg_fitness.append(get_population_fitness(pop))


    for i in pop: i.print_info()

    fig, ax = plt.subplots()
    ax.plot(avg_fitness)
    plt.show()


if __name__ == "__main__":
    main()
