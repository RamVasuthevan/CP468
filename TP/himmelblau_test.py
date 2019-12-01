from simple_genetic_algorithm import SGA

ALNUM = ["0", "1"]
VAR_STRING_LEN = 16
NUMBER_OF_VARIABLES = 2
VARIABLE_LEN = int(VAR_STRING_LEN / NUMBER_OF_VARIABLES)
PROBABILITY_OF_MUTATION = 0.005
NUM_STRINGS = 100
NUM_GENERATIONS = 100
DOMAIN_MIN = -6
DOMAIN_MAX = 6

#TODO docstring
def himmelblau(*xs):
    x = xs[0]
    y = xs[1]
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

print("Running Simple Genetic Algorithm on Himmelblau benchmark function")
SGA(himmelblau, NUM_STRINGS, ALNUM, VAR_STRING_LEN, VARIABLE_LEN, DOMAIN_MIN, DOMAIN_MAX, NUM_GENERATIONS,
    PROBABILITY_OF_MUTATION)
