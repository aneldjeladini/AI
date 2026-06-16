import pygad
import math
import random

N, M, R = map(float, input().split())
N = int(N)
M = int(M)

points = [tuple(map(float, input().split())) for _ in range(N)]


def decode(solution):
    umbrellas = []
    for i in range(0, len(solution), 3):
        x = solution[i]
        y = solution[i + 1]
        use = int(round(solution[i + 2]))
        if use == 1:
            umbrellas.append((x, y))
    return umbrellas


def fitness_func(ga, solution, idx):
    umbrellas = decode(solution)

    UNCOVERED_PENALTY = 10 ** 6
    penalty = 0

    for (px, py) in points:
        covered = False
        for (ux, uy) in umbrellas:
            if (ux - px) ** 2 + (uy - py) ** 2 < R ** 2:
                covered = True
                break
        if not covered:
            penalty += UNCOVERED_PENALTY

    LARGE_OVERLAP = 1000
    SMALL_OVERLAP = 100

    for i in range(len(umbrellas)):
        for j in range(i + 1, len(umbrellas)):
            dx = umbrellas[i][0] - umbrellas[j][0]
            dy = umbrellas[i][1] - umbrellas[j][1]
            d = math.sqrt(dx * dx + dy * dy)

            if d < (8 * R / 5):
                penalty += LARGE_OVERLAP
            elif d < (2 * R):
                penalty += SMALL_OVERLAP

    penalty += len(umbrellas) * 10

    return -penalty


gene_space = []
for _ in range(M):
    gene_space.extend([
        {'low': R, 'high': 10 - R},
        {'low': R, 'high': 10 - R},
        [0, 1]
    ])

params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,
    'num_genes': 3 * M,
    'gene_space': gene_space,
    'fitness_func': fitness_func,
    'mutation_num_genes': 1,
    'save_best_solutions': True
}

ga = pygad.GA(**params)
ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)
best_solutions = ga.best_solutions

print(solution)
print(fitness)


def random_chromosome():
    chrom = []
    for _ in range(M):
        x = random.uniform(R, 10 - R)
        y = random.uniform(R, 10 - R)
        use = random.choice([0, 1])
        chrom.extend([x, y, use])
    return chrom


candidates = [random_chromosome() for _ in range(300)]

candidates.sort(key=lambda c: fitness_func(None, c, 0))

chromosomes = []
last_fitness = None

for c in candidates:
    f = fitness_func(None, c, 0)
    if last_fitness is None or f > last_fitness + 1e-6:
        chromosomes.append(c)
        last_fitness = f
    if len(chromosomes) == 5:
        break

while len(chromosomes) < 5:
    chromosomes.append(random_chromosome())

    '''
    chromosomes = [

    [8.0, 8.0,  8.5, 8.0,  8.0, 8.5],

    [1.0, 1.0,  8.0, 8.0,  8.5, 8.5],

    [1.05, 1.0,  1.05, 1.0,  5.0, 5.0],

    [1.05, 1.0,  5.0, 5.0,  2.7, 1.0],

    [1.05, 1.0,  5.0, 5.0,  9.0, 9.0],
]'''

# submit_data(fitness_func, decode, chromosomes, best_solutions)