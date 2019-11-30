from simple_genetic_algorithm import SGA

ALNUM = ["0", "1"]
VAR_STRING_LEN = 8
VARIABLE_LEN = 4
PROBABILITY_OF_MUTATION = 0.5
PROBABILITY_OF_CROSSOVER = 0.75
NUM_STRINGS = 100
NUM_GENERATIONS = 100
DOMAIN_MIN = -2
DOMAIN_MAX = 2


def rosenbrock(*xs):
    """
    Takes in x, y cartesian values and returns function output

    Args:
        xs (List[num]): [x,y] x, y cartesian coordinates
    Returns:
        (float): f(x,y) = value closer to 0 indicates a coordinate closer to know global minimum
    """

    x = xs[0]
    y = xs[1]

    return (1-x)**2+100*(y-x**2)**2


print("Running Simple Genetic Algorithm on Rosenbrock benchmark function")

SGA(rosenbrock, NUM_STRINGS, ALNUM, VAR_STRING_LEN, VARIABLE_LEN, DOMAIN_MIN, DOMAIN_MAX, NUM_GENERATIONS,
    PROBABILITY_OF_MUTATION, PROBABILITY_OF_MUTATION)
