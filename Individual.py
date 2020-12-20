import random
import math

class Individual:

    def __init__(self, genesQuantity):
        self.genes = []
        self.fitness = 0
        for each in range(0, genesQuantity):
            self.genes.append(round(random.random(), 2))

    def getFitness(self):
        sigmaA = 0.0
        sigmaB = 0.0
        for gene in self.genes:
            sigmaA += gene**2.0
            sigmaB += math.cos(2.0*math.pi*gene)
        N = len(self.genes)#gene size
        return (-20.0*math.exp(-0.2*math.sqrt(sigmaA/N))-math.exp(sigmaB/N))

    #Now with minimisation
    def getFitnessOld(self):
        def d(x):
            return (x ** 2 - 10 * math.cos(2 * math.pi * x))
        return (len(self.genes) * 10) + sum([d(x) for x in self.genes])

    def printInfo(self):
        print("\nGenes: ", end="")
        print(self.genes, end=" ")
        print("Fitness = ", self.getFitness(), end="")

    def mutateGenes(self, mutationProb, mutationMagnitudeMax):
        tempGenes = []
        for individualGene in self.genes:
            tempGenes.append(self.mutateGene(individualGene, mutationProb, mutationMagnitudeMax))
        self.genes = tempGenes

    def mutateGene(self, gene, mutationProb, mutationMagnitudeMax):
        #decide how much the gene will mutate by
        mutationMagnitude = random.uniform(0, mutationMagnitudeMax)
        #pick rando number between 0 to 100
        if (random.randint(0, 100) < mutationProb):
            #mutate the gene
            if(random.randint(1,2)%2 == 0):
                if gene + mutationMagnitude > 32: gene = 32
                else: gene += mutationMagnitude
            else:
                if gene - mutationMagnitude < -32: gene = -32
                else: gene -= mutationMagnitude
        return gene

    #Pick random point in genes,
    def crossover(self, partner):
        crossoverPoint = random.randrange(0, len(self.genes))
        genes = [*self.genes[:crossoverPoint], *partner.genes[crossoverPoint:]]

        child1 = Individual(len(self.genes))
        child1.genes = genes

        genes = [*self.genes[crossoverPoint:], *partner.genes[:crossoverPoint]]
        child2 = Individual(len(self.genes))
        child2.genes = genes
        return (child1, child2)



