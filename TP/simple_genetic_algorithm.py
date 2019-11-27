from typing import List
import random
from TP.functions import general_decoder


def perform_reproduction(population, fitness_func) -> List:
    """#TODO update docstring
    Takes in mating pool of binary strings, and probabalistically selects a list of length, len(list_of_strings), 
    based on the relative fitness of each string

    Args:
        strings: List of binary strings that makes up the mating pool
        string2fitness: 
    Returns:
        new_generation_of_strings: List of binary strings
    """
    min_fitness = min(fitness_func(m) for m in population)
    fitnesses = [1 / (fitness_func(s) - min_fitness + 1) for s in population]
    total_fitness = sum(fitnesses)
    probabilities_of_reproduction = [fit / total_fitness for fit in fitnesses]
    return random.choices(population=population, weights=probabilities_of_reproduction, k=len(population))


def perform_mutations(list_of_strings, probability_of_mutation, alphabet):
    """
    Takes a list of strings, returns a list of potentially mutated binary strings

    Args:
        string: List of binary strings to mutate
    Returns:
        new_list_of_strings: List of potentially mutated binary strings
    """
    return [attempt_mutation(s, probability_of_mutation, alphabet) for s in list_of_strings]


def perform_mating(list_of_strings, probability_of_crossover):
    """
    Takes a list of strings, returns a list of binary strings after crossover operation

    Args:
        list_of_strings: List of binary strings to mate
    Returns:
        new_list_of_strings: List of binary strings after crossover operation
    """
    new_list_of_strings = []

    while (len(list_of_strings) > 0):
        s1 = list_of_strings.pop(random.randint(0, len(list_of_strings) - 1))
        s2 = list_of_strings.pop(random.randint(0, len(list_of_strings) - 1))

        s1p, s2p = crossover_pair(s1, s2, probability_of_crossover)
        new_list_of_strings.append(s1p)
        new_list_of_strings.append(s2p)

    return new_list_of_strings


def attempt_mutation(s, probability_of_mutation, alphabet):
    """
    Takes a string to perform low probability bit mutation on

    Args:
        s: Binary string to mutate
    Returns:
        new_string: Mutated binary string
    """
    # bit flipping
    if random.random() < probability_of_mutation:
        bit_to_flip = random.randint(0, len(s) - 1)
        s = list(s)
        s[bit_to_flip] = random.choice(alphabet)
        return "".join(s)
    else:
        return s


def crossover_pair(s1, s2, probability_of_crossover):
    """
    Takes two strings for crossover. Randomly selects a crossover point between 1 and len(s1)-1. 
    Performs crossover on and returns both new strings.
    Assumes len(s1) = len(s2)

    Args:
        s1: Binary string for mating crossover
        s2: Binary string for mating crossover
    Returns:
        s1p: Binary string from mating crossover
        s2p: Binary string from mating crossover
    """
    if random.random() < probability_of_crossover:
        crossover_point = random.randint(1, len(s1) - 2)
        s1p = s1[:crossover_point] + s2[crossover_point:]
        s2p = s2[:crossover_point] + s1[crossover_point:]
    else:
        s1p = s1
        s2p = s2
    return (s1p, s2p)


def initialize(num_strings: int, alphabet: List[str], string_length) -> List[str]:
    """
    Generates num_strings of random binary strings with characters in alphabet

    Args:
        num_strings: Number of string to be generated 
        alphabet: Valid characters
    Returns:
        List of num_strings random binary strings with characters in alphabet
    """
    return ["".join(random.choices(alphabet, k=string_length)) for _ in range(num_strings)]


def print_table(strings, test_func, fitness_func, decoder_func):
    """ 
    Pretty prints tested binary string mating pools and each string's reproduction performance stats

    Args:
        strings: List of binary strings that makes up the mating pool
        test_func: Function used to test found fitness  ex: Himmelblau (1000 - 0) 
                    Results closer to zero are closer to optimization
        fitness_func: Compares fitness measure to benchmark of optimization  ex: Himmelblau (0 - 1000)
                    Higher values are higher fitness
        decoder_func: Used to decode binary strings into integers
    Prints:
        Table containing binary string; its performed fitness level with the test function; 
        (x, y) cartesian coordinates used as inputs for test function; result of measured fitness compared to benchmark
        value; and the likelihood that the string will reproduce, as a proportion of its fitness to the accumulated
        fitness of its mating pool.
    """
    total_fitness = sum([fitness_func(test_func(*decoder_func(s))) for s in strings])
    proportion = [0 if total_fitness == 0 else fitness_func(test_func(*decoder_func(s))) / total_fitness for s in
                  strings]

    print("{:11}{:11}{:11}{:11}{:>15}".format("String", "Fitness", "Coord", "Result", "Proportion of total"))
    print("=" * 65)
    for s, p in zip(strings, proportion):
        print(
            "{:11s}{:<11}{}{:4}{:<11}{:>.15f}".format(s, fitness_func(test_func(*decoder_func(s))), decoder_func(s), "",
                                                      test_func(*decoder_func(s)),
                                                      p))
    # TODO wasn't able to figure out how to format print a tuple with padding so that the last 2 columns would look
    #  consistent
    print("=" * 65)
    print("")


# program starts here:
# -------------------------------------------------------------------------------------------------------------------------------------------
def SGA(test_function, num_strings, alphabet, string_length, variable_length, domain_start, domain_end,
        number_of_generations, probability_of_mutation, probability_of_crossover):
    population = initialize(num_strings, alphabet, string_length)
    fitness = lambda string: test_function(*general_decoder(string, variable_length, domain_start, domain_end))

    for i in range(number_of_generations):
        population = perform_reproduction(population, fitness)
        population = perform_mating(population, probability_of_crossover)
        population = perform_mutations(population, probability_of_mutation, alphabet)

        min_fitness = min(fitness(m) for m in population)
        for m in population:
            if fitness(m) == min_fitness:
                best_individual = general_decoder(m, variable_length, domain_start, domain_end)
        print("Generation ", i, ":")
        print("Best Individual: ", best_individual)
        print("Fitness: ", min_fitness)
