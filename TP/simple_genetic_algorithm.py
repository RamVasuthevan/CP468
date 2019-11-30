from typing import List
import random
from functions import general_decoder


def initialize(num_strings: int, alnum_set: List[str], var_string_length) -> List[str]:
    """
    Generates num_strings of random strings with characters of their alphanumeric character set

    Args:
        num_strings (int): Number of strings to be generated 
        alnum_set (List[str]): Valid characters to genrate random string from
        var_string_length (int): Number of characters expected to be in each string
    Returns:
        (List[str]): List of num_strings random strings made with characters of their alphanumeric character set
    """

    return ["".join(random.choices(alnum_set, k=var_string_length)) for _ in range(num_strings)]


def perform_reproduction(population, fitness_func) -> List:
    """
    Takes in a population of strings and probabalistically candidates for mating  based on the 
    relative fitness of each string (i.e. the more fit members of the population will be picked more often
    and will therefore make up a bigger portion of the mating pool)

    Args:
        population (List[str]): List of strings that make up the mating pool
        fitness_func (<function>): Benchmark function with known global minima; returned values
                                    closer to zero mean the given arguments are closer to optimum
                                Args:
                                    (str): Alphanumeric string representing a number system value(s)
                                Returns:
                                    (float): floating point value between 0 to 1; results closer to zero are closer to optimization
    Returns:
        (List[str]): List of strings that make up the new mating pool generation
    """

    #determine the minimum found fitness within the population
    min_fitness = min(fitness_func(m) for m in population)

    #compile a list of all found fitness values of the population as a measure of it against the su
    #compile a list of floating point values between 0 to 1, numbers closer to 0 have a higher fitness 
    fitnesses = [1 / (fitness_func(s) - min_fitness + 1) for s in population]

    #sum up all found fitness measures 
    total_fitness = sum(fitnesses)

    #creates a list of each fitness measure's proportion to the sum of all found fitness measures of 
    #the mating pool
    probabilities_of_reproduction = [fit / total_fitness for fit in fitnesses]

    #create list of randomly chosen strings that are weight biased 
    return random.choices(population=population, weights=probabilities_of_reproduction, k=len(population))


def perform_mating(population, probability_of_crossover):
    """
    Takes a list of binary strings, returns a list of binary strings after potential crossover operations

    Args:
        population (List[str]): List of strings that make up the mating pool
        probability_of_crossover (float): decimal number between 0 and 1 that represents the liklihood
                                            that 2 randomly selected members of the mating pool will 
                                            perform a crossover of characters
    Returns:
        (List[str]): List of strings that make up the now potentially modified mating pool 
    """

    new_pop = []

    while (len(population) > 0):
        s1 = population.pop(random.randint(0, len(population) - 1))
        s2 = population.pop(random.randint(0, len(population) - 1))

        s1p, s2p = crossover_pair(s1, s2, probability_of_crossover)
        new_pop.append(s1p)
        new_pop.append(s2p)

    return new_pop


def crossover_pair(s1, s2):
    """
    Takes two strings for crossover. Randomly determines if the selects a crossover point 
    between 1 and len(s1)-1. Compares probability_of_crossover > random floating point between [0.0, 1.0)
    and performs crossover of characters and returns 2 new strings if condition is true.
    Assumes len(s1) = len(s2)

    Args:
        s1: Binary string for mating crossover
        s2: Binary string for mating crossover
    Returns:
        s1p: Binary string from mating crossover
        s2p: Binary string from mating crossover
    """
    crossover_point = random.randint(1, len(s1) - 2)
    s1p = s1[:crossover_point] + s2[crossover_point:]
    s2p = s2[:crossover_point] + s1[crossover_point:]

    return (s1p, s2p)


def perform_mutations(population, probability_of_mutation, alnum_set):
    """
    Takes a list of binary strings, returns a list of binary strings after potential crossover operations

    Args:
        population (List[str]): List of strings that make up the mating pool
        probability_of_crossover (float): decimal number between 0 and 1 that represents the liklihood
                                            that 2 randomly selected members of the mating pool will 
                                            perform a crossover of characters

    Args:
        population (List[str]): List of strings that make up the mating pool
        probability_of_mutation (float): decimal number between 0 and 1 that represents the liklihood
                                            that a character will mutate into another character from
                                            its alphanumeric character set
        alnum_set (List[str]): 
    Returns:
        (List[str]): List of strings that make up the mating pool
    """

    return [attempt_mutation(s, probability_of_mutation, alnum_set) for s in population]


def attempt_mutation(s, probability_of_mutation, alnum_set):
    """
    Takes a string to perform low probability bit mutation on

    Args:
        s: Binary string to mutate
        probability_of_mutation (float):
        alnum_set (List[str]): Valid alphanumeric characters to genrate number-system value-strings from 
    Returns:
        new_string: Mutated binary string
    """

    # bit flipping
    if random.random() < probability_of_mutation:
        bit_to_flip = random.randint(0, len(s) - 1)
        s = list(s)
        s[bit_to_flip] = random.choice(alnum_set)
        return "".join(s)
    else:
        return s


def print_table(strings, test_func, fitness_func, decoder_func):
    """ 
    Pretty prints tested binary string mating pools and each string's reproduction performance stats

    Args:
        strings: List of binary strings that makes up the mating pool
        test_func: Function used to test found fitness  ex: Himmelblau (1000 - 0) 
                    Results closer to zero are closer to optimization
        fitness_func <function>: Compares fitness measure to benchmark of optimization  ex: Himmelblau (0 - 1000)
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
#TODO docstring
def SGA(test_function, num_strings, alnum_set, var_string_length, variable_length, domain_min, domain_max,
        number_of_generations, probability_of_mutation, probability_of_crossover):
    """
    Simple Genetic Algorithm that finds optimal 

    Args:
        test_function (<function>): Benchmark function that has known optimum values (global min)
        num_strings (int): the number of strings to create
        alnum_set (List[str]): Valid alphanumeric characters to genrate number system value-strings from 
        var_string_length (int): character length of string that contains one or more number system value-string string variables
        variable_length (int): character length of one number system value-string variable
        domain_min (Union[float,int]): min value of operational domain
        domain_max (Union[float,int]): max value of operational domain
        number_of_generations (int): number of times to mate / mutate the poulation in the attempt to hone in
                                        on the optimal input values for the given test_function
        probability_of_mutation (float):
        probability_of_crossover (float):
    Returns:
        None
    """
    
    #initialize a random population of num_strings values to be the starting point for optimization attempt
    #returns string with (var_string_length * num_strings) number of characters
    population = initialize(num_strings, alnum_set, var_string_length)

    #small anonymous function used to find fitness measures of a member of a mating pool population, 
    #determined by the given benchmark test function
    fitness = lambda string: test_function(*general_decoder(string, variable_length, domain_min, domain_max, len(alnum_set)))
    
    #print results
    print("\nTested population size: ", num_strings, ", Number of generations: ", number_of_generations)
    print("\nGeneration \t Strongest Candidate \t Fitness")
    print("="*100)

    #TODO docstring
    for i in range(number_of_generations):
        population = perform_reproduction(population, fitness)
        population = perform_mating(population, probability_of_crossover)
        population = perform_mutations(population, probability_of_mutation, alnum_set)

        min_fitness = min(fitness(m) for m in population)
        
        #print perfromance of poulation
        for m in population:
            if fitness(m) == min_fitness:
                best_individual = general_decoder(m, variable_length, domain_min, domain_max, len(alnum_set))
        print("{:<10d} \t {} \t {} \t".format(i, best_individual, min_fitness))
    
    print("="*100)
    print("")