#Simple genetic algorithm
import random
from Individual import Individual
from Population import Population
import matplotlib.pyplot as plt
import numpy as np



#Tournament selection
def tournament(Population):
    children =[]
    for individual in Population:
        #Grab two random individuals from the population
        child1 = Population[random.randint(0, (len(Population)- 1))]
        child2 = Population[random.randint(0, (len(Population)- 1))]

        if child1.getFitness() > child2.getFitness():
            children.append(child1)
        else:
            children.append(child2)
    return children



def main():
    #Creating a population:
    print("Original Population: ")

    myPop = Population(50, 10)


    avgFitness =[]

    for i in range(0, 100):
        myPop.tournamentPopulation()
        #myPop.crossoverPopulation()
        #myPop.mutatePopulation(50, 1)

        avgFitness.append(myPop.getPopulationFitness()/len(myPop.populationList))

    myPop.printPopulation()
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(avgFitness)
    plt.show()#show

if __name__ == "__main__":
    main()




