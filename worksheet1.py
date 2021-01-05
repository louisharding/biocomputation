# Simple genetic algorithm
import random
from Individual import Individual
from Population import Population
import matplotlib.pyplot as plt
import numpy as np


# Tournament selection
def tournament(Population):
    children = []
    for individual in Population:
        # Grab two random individuals from the population
        child1 = Population[random.randint(0, (len(Population) - 1))]
        child2 = Population[random.randint(0, (len(Population) - 1))]

        if child1.get_fitness() > child2.get_fitness():
            children.append(child1)
        else:
            children.append(child2)
    return children







def main():
    # make a population list comprising of individuals
    pop = [Individual(10) for i in range(50)]

    for i in pop:
        i.print_info()


    # myPop = Population(50, 10)
    # myPop.print_population()
    # avg_fitness = []
    #
    # for i in range(0, 100):
    #     myPop.tournament_population()
    #     myPop.mutate_population(5, 1)
    #     myPop.crossover_population()
    #     avg_fitness.append(myPop.get_population_fitness() / len(myPop.populationList))
    #
    # fig, ax = plt.subplots()
    # ax.plot(avg_fitness)
    # plt.show()


if __name__ == "__main__":
    main()
