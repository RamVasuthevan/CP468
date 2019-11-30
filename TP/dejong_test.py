from simple_genetic_algorithm import SGA

ALNUM = ["0", "1"]
VAR_STRING_LEN = 40
VARIABLE_LEN = 10
PROBABILITY_OF_MUTATION = 0.05
PROBABILITY_OF_CROSSOVER = .8
NUM_STRINGS = 100
NUM_GENERATIONS = 100
DOMAIN_MIN = -5.12
DOMAIN_MAX = 5.12

#TODO docstring
def dejong(*xs):
    return sum(xi ** 2 for xi in xs)

print("Running Simple Genetic Algorithm on De Jong Sphere benchmark function")
SGA(dejong, NUM_STRINGS, ALNUM, VAR_STRING_LEN, VARIABLE_LEN, DOMAIN_MIN, DOMAIN_MAX, NUM_GENERATIONS,
    PROBABILITY_OF_MUTATION, PROBABILITY_OF_MUTATION)
