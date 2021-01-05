import math

N = 5

genes = [1, 2, 3, 4, 3]

def get_fitness():
    sigma_a = 0.0
    sigma_b = 0.0
    for gene in genes:
        sigma_a += gene ** 2.0
        sigma_b += math.cos(2.0 * math.pi * gene)
    n = len(genes)  # gene size
    return -20 * math.exp(-0.2 * math.sqrt(sigma_a / n)) - math.exp(sigma_b / n)

def f():
    return -20 * \
           math.exp(-0.2 * math.sqrt(sum([x ** 2 for x in genes]) / N)) \
           - math.exp(sum(math.cos(math.pi * x * 2) for x in genes) / N)

print(f())
print(get_fitness())