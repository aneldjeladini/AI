from constraint import *

def differentColors(color_1, color_2):
    return color_1 != color_2


if __name__ == "__main__":

    problem = Problem()

    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    problem.addVariables(variables, ["R","G","B"])

    pairs = [("WA","NT"), ("WA","SA"), ("NT","SA"), ("NT","Q"), ("SA","Q"), ("SA","NSW"),("SA","V"), ("Q","NSW"),("NSW","V")]

    for pair in pairs:
        problem.addConstraint(differentColors,pair)

    print(problem.getSolution())

    print(problem.getSolution())

    res_iter = problem.getSolutionIter()
    for i in range(5):
        print(next(res_iter))