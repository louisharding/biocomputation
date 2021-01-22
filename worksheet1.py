# Simple genetic algorithm
import random
from Individual import Individual
import matplotlib.pyplot as plt



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
    # make a population list comprising of individuals with a 10-long genome
    pop = []
    for _ in range(0, 50):
        pop.append(Individual())



    avg_fitness = []
    for i in range(0, 300):
        # tournament
        pop = tournament(pop)
        # mutate
        pop = [x.mutate_genes(10, 4) for x in pop]
        # crossover
        pop = crossover(pop)
        avg_fitness.append(get_population_fitness(pop)/len(pop))



    fig, ax = plt.subplots()
    ax.plot(avg_fitness)
    plt.show()


if __name__ == "__main__":
    main()
