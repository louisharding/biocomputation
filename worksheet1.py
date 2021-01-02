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
    # Creating a population:
    myPop = Population(50, 10)

    print("Original Population: ")
    myPop.print_population()

    avgFitness = []

    for i in range(0, 100):
        myPop.tournament_population()
        myPop.mutate_population(5, 1)
        #myPop.crossover_population()
        avgFitness.append(myPop.get_population_fitness() / len(myPop.populationList))

    myPop.print_population()
    fig, ax = plt.subplots()  # Create a figure containing a single axis.
    ax.plot(avgFitness)
    plt.show()  # show


if __name__ == "__main__":
    main()
