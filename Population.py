import random
import math
from Individual import Individual
#commiting git 20 dec
class Population:

    def __init__(self, populationSize, genesQuantity):
        self.populationList = []
        self.populationFitness = 0
        for each in range (0, populationSize):
            self.populationList.append(Individual(genesQuantity))

    def getPopulationFitness(self):
        tempFitness = 0
        for individual in self.populationList:
            tempFitness += individual.getFitness()
        return tempFitness

    def  printPopulation(self):
        # Print each indiviual of the population
        print("The population: ")
        for individual in self.populationList:
            individual.printInfo()

    #Tournament
    def tournamentPopulation(self):
        tempPopulation = []
        for each in range(0, len(self.populationList)):
            #pick random two individuals,
            child1 = self.populationList[random.randint(0, len(self.populationList) - 1)]
            child2 = self.populationList[random.randint(0, len(self.populationList) - 1)]

            if (child1.getFitness() < child2.getFitness()):
                tempPopulation.append(child1)
            else:
                tempPopulation.append(child2)
        self.populationList = tempPopulation


    #Crossover
    def crossoverPopulation(self):
        for individual in self.populationList:
            randomPartner = self.populationList[random.randint(0, len(self.populationList)-1)]
            individual.crossover(randomPartner)

        pass
    #Mutation
    def mutatePopulation(self, mutationRate, mutationMagnitudeMax):
        for individual in self.populationList:
            individual.mutateGenes(mutationRate, mutationMagnitudeMax)




