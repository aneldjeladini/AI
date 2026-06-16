from constraint import Problem, BacktrackingSolver

if __name__ == '__main__':
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(K)]
    N = max(map(max, grid))  # Number of regions

    problem = Problem(solver=BacktrackingSolver())

    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.
    # 0 -> no star, 1 -> star (sekoj red)
    for r in range(K):
        for c in range(K):
            problem.addVariable((r, c), [0, 1])

    #helper
    region_cells = {}
    for r in range(K):
        for c in range(K):
            reg = grid[r][c]
            if reg not in region_cells:
                region_cells[reg] = []
            region_cells[reg].append((r, c))



    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.

    # N dzvezdi -> edna po region vo prosek &&
    # najmnogu 2 po region -> raspredeli gi po site regioni
    all_cells = [(r, c) for r in range(K) for c in range(K)]
    problem.addConstraint(lambda *vals: sum(vals) == N, all_cells)

   # sekoj region ima max 2 dzvezdi
    for reg, cells in region_cells.items():
        problem.addConstraint(lambda *vals: sum(vals) <= 2, cells)

    # dzvezdi od razlicni regioni ne smeat da bidat na ist red/kolona
    def no_shared_line(n_first):
        def constraint(*vals):
            first_group_has_star  = sum(vals[:n_first]) > 0
            second_group_has_star = sum(vals[n_first:]) > 0
            return not (first_group_has_star and second_group_has_star)
        return constraint

    def add_line_constraints(line_cells):
        # grupiraj gi kjeliite vo ovaa linija po region
        by_region = {}
        for (r, c) in line_cells:
            reg = grid[r][c]
            if reg not in by_region:
                by_region[reg] = []
            by_region[reg].append((r, c))

        regions = list(by_region.keys())
        # proveri go sekoj par od razlicni regioni vo ovaa linija
        for i in range(len(regions)):
            for j in range(i + 1, len(regions)):
                cells_a = by_region[regions[i]]
                cells_b = by_region[regions[j]]
                problem.addConstraint(
                    no_shared_line(len(cells_a)),
                    cells_a + cells_b
                )

    for r in range(K):
        add_line_constraints([(r, c) for c in range(K)])  # sekoj red

    for c in range(K):
        add_line_constraints([(r, c) for r in range(K)])  # sekoja kolona

    # Dve dzvezdi bo ist region ne smeat da bidat ortogonalni sosedi (gore,dole,levo,desno),smeat samo dijagonalno
    orthogonal_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for reg, cells in region_cells.items():
        cells_set = set(cells)
        for (r, c) in cells:
            for (dr, dc) in orthogonal_directions:
                neighbour = (r + dr, c + dc)
                # Dodadi uslov ednas po par
                if neighbour in cells_set and neighbour > (r, c):
                    problem.addConstraint(
                        lambda a, b: not (a == 1 and b == 1),
                        [(r, c), neighbour]
                    )


    result = problem.getSolution()

    # Ispechatete go reshenieto vo baraniot format.
    # Print the solution in the required format.

    if result is None:
        print("No Solution!")
    else:
        for r in range(K):
            row_out = []
            for c in range(K):
                if result[(r, c)] == 1:
                    row_out.append('*')
                else:
                    row_out.append(str(grid[r][c]))
            print(' '.join(row_out))