import pygad

N = int(input())
S, E = map(int, input().split())
dist = [list(map(float, input().split())) for _ in range(N)]


cities = []
for i in range(N):
    if i != S and i != E:
        cities.append(i)


def decode(solution):

    friend1 = []
    friend2 = []

    for i in range(len(solution)):
        gene = solution[i]
        city = cities[i]

        if gene < 0.5:
            friend1.append([city, gene])
        else:
            friend2.append([city, gene])

    for i in range(len(friend1)):
        for j in range(i + 1, len(friend1)):
            if friend1[i][1] > friend1[j][1]:
                temp = friend1[i]
                friend1[i] = friend1[j]
                friend1[j] = temp

    for i in range(len(friend2)):
        for j in range(i + 1, len(friend2)):
            if friend2[i][1] > friend2[j][1]:
                temp = friend2[i]
                friend2[i] = friend2[j]
                friend2[j] = temp


    route1 = [S]
    route2 = [S]

    for i in range(len(friend1)):
        route1.append(friend1[i][0])

    for i in range(len(friend2)):
        route2.append(friend2[i][0])

    route1.append(E)
    route2.append(E)

    return route1, route2


def route_cost(route):
    total = 0
    for i in range(len(route) - 1):
        total += dist[route[i]][route[i + 1]]
    return total


def fitness_func(ga, solution, idx):

    route1, route2 = decode(solution)

    time1 = route_cost(route1)
    time2 = route_cost(route2)

    makespan = time1
    if time2 > makespan:
        makespan = time2

    diff = len(route1) - len(route2)
    if diff < 0:
        diff = -diff
    imbalance_penalty = diff * 5

    if time1 > time2:
        ratio = time1 / time2
    else:
        ratio = time2 / time1

    overload_penalty = 0
    if ratio > 2:
        overload_penalty = 1000

    cost = makespan + imbalance_penalty + overload_penalty

    return 1 / (1 + cost)


gene_space = []
for i in range(N - 2):
    gene_space.append({'low': 0.0, 'high': 1.0})


params = {
    'num_generations': 500,
    'sol_per_pop': 100,
    'num_parents_mating': 50,
    'num_genes': N - 2,
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

route1, route2 = decode(solution)

print("Friend 1 route:", route1)
print("Friend 2 route:", route2)
print("Fitness:", fitness)

# submit_data(fitness_func, decode, best_solutions)