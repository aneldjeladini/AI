import pygad
import numpy as np

if __name__ == '__main__':

    num_machines = int(input())
    machines = []

    type_to_id = {}
    id_to_type = []

    for _ in range(num_machines):
        t, c = input().split()
        t = int(t)

        if c not in type_to_id:
            type_to_id[c] = len(id_to_type)
            id_to_type.append(c)

        machines.append((t, type_to_id[c]))


    def fitness_func(ga_instance, solution, solution_idx):

        n = num_machines

        perm = solution[:n]
        p_type = int(solution[n])

        preferred_type = p_type

        total_cost = 0

        perm = np.array(perm).astype(int)

        used = set()
        cleaned = []

        for x in perm:
            if 0 <= x < n and x not in used:
                cleaned.append(x)
                used.add(x)

        for i in range(n):
            if i not in used:
                cleaned.append(i)

        perm = cleaned

        for i in range(0, n, 4):
            team = perm[i:i+4]

            if len(team) < 4:
                continue

            times = [machines[idx][0] for idx in team]
            types = [machines[idx][1] for idx in team]

            if all(t == preferred_type for t in types):
                cost = min(times)
            else:
                cost = max(times)

            total_cost += cost

        return -total_cost


    params = {
        'num_generations': 300,
        'sol_per_pop': 50,
        'num_parents_mating': 20,

        'num_genes': num_machines + 1,

        'gene_space': [list(range(num_machines))] * num_machines +
                      [list(range(len(id_to_type)))],

        'fitness_func': fitness_func,
        'mutation_num_genes': 1
    }


    ga = pygad.GA(**params)
    ga.run()


    best_solution, _, _ = ga.best_solution()

    perm = best_solution[:num_machines]
    perm = np.array(perm).astype(int)

    p_type = id_to_type[int(best_solution[num_machines])]

    used = set()
    clean_perm = []

    for x in perm:
        if 0 <= x < num_machines and x not in used:
            clean_perm.append(x)
            used.add(x)

    for i in range(num_machines):
        if i not in used:
            clean_perm.append(i)

    perm = clean_perm


    teams = []
    total = 0

    for i in range(0, num_machines, 4):
        team = perm[i:i+4]

        if len(team) < 4:
            continue

        teams.append(team)

        times = [machines[idx][0] for idx in team]
        types = [machines[idx][1] for idx in team]

        if all(t == type_to_id[p_type] for t in types):
            total += min(times)
        else:
            total += max(times)


    print(total)
    print(p_type)

    for team in teams:
        print(*team)