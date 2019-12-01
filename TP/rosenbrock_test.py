from simple_genetic_algorithm import SGA

ALNUM = ["0", "1"]
VAR_STRING_LEN = 16
NUMBER_OF_VARIABLES = 2
VARIABLE_LEN = int(VAR_STRING_LEN / NUMBER_OF_VARIABLES)
PROBABILITY_OF_MUTATION = 0.01
POP_SIZE = 100
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

SGA(rosenbrock, POP_SIZE, ALNUM, VAR_STRING_LEN, VARIABLE_LEN, DOMAIN_MIN, DOMAIN_MAX, NUM_GENERATIONS,
    PROBABILITY_OF_MUTATION)
