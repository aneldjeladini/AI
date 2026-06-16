import pygad


def read_input():
    M, N = map(int, input().split())
    K = int(input())
    B = int(input())

    unusable = set()
    for _ in range(B):
        r, c = map(int, input().split())
        unusable.add((r, c))

    return M, N, K, unusable


def fitness_func(ga_instance, solution, solution_idx):
    sprinklers = []

    for gene in solution:
        if gene == -1:
            continue
        r = gene // N
        c = gene % N
        sprinklers.append((r, c))

    all_cells = {(r, c) for r in range(M) for c in range(N)}
    crops = all_cells - unusable

    watered = set()

    directions = []
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            if abs(dr) + abs(dc) <= 2:
                directions.append((dr, dc))

    for r, c in sprinklers:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N:
                watered.add((nr, nc))

    destroyed = set(sprinklers) & crops
    valid_watered = (watered & crops) - destroyed

    used_sprinklers = len(sprinklers)

    return len(valid_watered) - 0.01 * used_sprinklers


if __name__ == "__main__":
    M, N, K, unusable = read_input()

    params = {
        'num_generations': 100,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': K,
        'gene_space': list(range(M * N)) + [-1],
        'fitness_func': fitness_func,
        'mutation_num_genes': 1
    }

    ga = pygad.GA(**params)
    ga.run()

    best_solution, _, _ = ga.best_solution()

    sprinklers = []
    for gene in best_solution:
        if gene == -1:
            continue
        r = gene // N
        c = gene % N
        sprinklers.append((r, c))

    all_cells = {(r, c) for r in range(M) for c in range(N)}
    crops = all_cells - unusable

    watered = set()

    directions = []
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            if abs(dr) + abs(dc) <= 2:
                directions.append((dr, dc))

    for r, c in sprinklers:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N:
                watered.add((nr, nc))

    destroyed = set(sprinklers) & crops
    valid_watered = (watered & crops) - destroyed

    print(len(valid_watered), len(sprinklers))
    for r, c in sprinklers:
        print(r, c)
