#rosenbrock_test.py
from simple_genetic_algorithm import SGA

ALNUM = ["0", "1"]
VAR_STRING_LEN = 16
NUMBER_OF_VARIABLES = 2
VARIABLE_LEN = int(VAR_STRING_LEN / NUMBER_OF_VARIABLES)
PROBABILITY_OF_MUTATION = 0.01
POP_SIZE = 100
NUM_GENERATIONS = 1000
DOMAIN_MIN = -2
DOMAIN_MAX = 2


def rosenbrock(*xs):
    """
    The function is defined on n-dimensional space.
    The function can be defined on any input domain but it is usually evaluated on
    x_i element of [-5, 10] for i = 1, ..., n.
    
    Takes in n dimensional coordinates and returns output of: 
        f(x,y) = sum[b(x_i + 1 - (x_i)^2)^2 + (a - x_i)^2]]
    for i = 1, ..., n; and the parameters a and b are constants set to a = 1 and b = 100..

    The function has one global minimum f(x^*) = 0 at x^* = (1, ..., 1).

    Args:
        xs (List[num]): n dimensional coordinates for Euclidean (n + 1)-space
    Returns:
        (float): f(x,y) = value closer to 0 indicates a coordinate closer to know global minimum
    """

    x = xs[0]
    y = xs[1]

    return (1-x)**2+100*(y-x**2)**2


print("Running Simple Genetic Algorithm on Rosenbrock benchmark function")

SGA(rosenbrock, POP_SIZE, ALNUM, VAR_STRING_LEN, VARIABLE_LEN, DOMAIN_MIN, DOMAIN_MAX, NUM_GENERATIONS,
    PROBABILITY_OF_MUTATION)

print("\nRosenbrock benchmark test complete\n")
