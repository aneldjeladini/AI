from constraint import *

if __name__ == "__main__":

    problem = Problem(BacktrackingSolver())

    variables = range(16)
    domain = range(1,17)

    problem.addVariables(variables,domain)

    sum = 34

    for first in [0,4,8,2]:
        row_vars = [first + move for move in range(4)]
        problem.addConstraint(ExactSumConstraint(sum), row_vars)

    for first in [0, 1, 2, 3]:
        col_vars = [first + move for move in range(0, 16, 4)]
        problem.addConstraint(ExactSumConstraint(sum), col_vars)

    main_diag_vars = [move for move in range(0, 16, 5)]
    minor_diag_vars = [3 + move for move in range(0, 12, 3)]

    problem.addConstraint(ExactSumConstraint(sum), main_diag_vars)
    problem.addConstraint(ExactSumConstraint(sum), minor_diag_vars)

    problem.addConstraint(AllDifferentConstraint(), variables)

    print(problem.getSolution())

