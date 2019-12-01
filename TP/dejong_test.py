from simple_genetic_algorithm import SGA

ALNUM = ["0", "1"]
VAR_STRING_LEN = 20
NUMBER_OF_VARIABLES = 4
VARIABLE_LEN = int(VAR_STRING_LEN / NUMBER_OF_VARIABLES)
PROBABILITY_OF_MUTATION = 0.05
POP_SIZE = 40
NUM_GENERATIONS = 1000
DOMAIN_MIN = -5.12
DOMAIN_MAX = 5.12

#TODO docstring
def dejong(*xs):
    return sum(xi ** 2 for xi in xs)

print("Running Simple Genetic Algorithm on De Jong Sphere benchmark function")
SGA(dejong, POP_SIZE, ALNUM, VAR_STRING_LEN, VARIABLE_LEN, DOMAIN_MIN, DOMAIN_MAX, NUM_GENERATIONS,
    PROBABILITY_OF_MUTATION)

dejong(dejong(-0.3200 ,-0.3200 ,0.0000 ,0.0000))