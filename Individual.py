import random
import math


def mutate_gene(gene, mutation_prob, mutation_magnitude_max):
    # decide how much the gene will mutate by
    mutation_magnitude = random.uniform(0, mutation_magnitude_max)
    # pick random number between 0 to 100
    if random.randint(0, 100) < mutation_prob:
        # mutate the gene
        if random.randint(1, 2) % 2 == 0:
            if gene + mutation_magnitude > 32:
                gene = 32
            else:
                gene += mutation_magnitude
        else:
            if gene - mutation_magnitude < -32:
                gene = -32
            else:
                gene -= mutation_magnitude
    return gene


class Individual:
    def __init__(self, genes_quantity):
        self.genes = []
        self.fitness = 0
        for each in range(0, genes_quantity):
            self.genes.append(round(random.random(), 2))

    def get_fitness(self):
        sigma_a = 0.0
        sigma_b = 0.0
        for gene in self.genes:
            sigma_a += gene ** 2.0
            sigma_b += math.cos(2.0 * math.pi * gene)
        n = len(self.genes)  # gene size
        return -20.0 * math.exp(-0.2 * math.sqrt(sigma_a / n)) - math.exp(sigma_b / n)

    def print_info(self):
        print("\nGenes: ", end="")
        print(self.genes, end=" ")
        print("Fitness = ", self.get_fitness(), end="")

    def mutate_genes(self, mutation_prob, mutation_magnitude_max):
        temp_genes = []
        for individualGene in self.genes:
            temp_genes.append(mutate_gene(individualGene, mutation_prob, mutation_magnitude_max))
        self.genes = temp_genes

    # Pick random point in self.genes,
    def crossover(self, partner):
        crossover_point = random.randint(0, len(self.genes)-1)
        genes = [*self.genes[:crossover_point], *partner.genes[crossover_point:]]
        child1 = Individual(len(self.genes))
        child1.genes = genes
        genes = [*self.genes[crossover_point:], *partner.genes[:crossover_point]]
        child2 = Individual(len(self.genes))
        child2.genes = genes

        return child1, child2
