import random
import math

N = 50


class Individual:
    def __init__(self, genes=None):
        if genes is None:
            self.genes = [random.uniform(-32, 32) for i in range(N)]
        else:
            self.genes = genes

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
        m = random.uniform(0, mutation_magnitude_max)
        temp_genes = []
        for gene in self.genes:
            if random.randint(0, 100) < mutation_prob:
                if random.randint(1, 2) % 2 == 0:
                    temp_genes.append(min(gene + m, 32))
                else:
                    temp_genes.append(max(gene - m, -32))
            else:
                temp_genes.append(gene)
        i = Individual(10)
        i.genes = temp_genes
        return Individual(temp_genes)


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
