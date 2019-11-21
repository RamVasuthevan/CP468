from typing import Tuple, List, Dict
import random
import heapq
from math import ceil, log
import sys
from functions import himmelblau, fitness_func, functionWithDomain, string2fitness, DOMAIN, MAX_VAL, decode_himmelblau


BIN_ALPHABET = ["0","1"]
STRING_LEN = (ceil(log(DOMAIN, 2))+1)*2

PROBABILITY_OF_MUTATION = 0.001
NUM_STRINGS = 10
NUM_GENERATIONS = 50

def perform_reproduction(strings, string2fitness) -> List:
    """#TODO update docstring
    Takes in mating pool of binary strings, and probabalistically selects a list of length, len(list_of_strings), 
    based on the relative fitness of each string

    Args:
        strings: List of binary strings that makes up the mating pool
        string2fitness: 
    Returns:
        new_generation_of_strings: List of binary strings
    """
    fitnesses = [ string2fitness(s) for s in strings]
    total_fitness = sum(fitnesses)
    probabilities_of_reproduction = [0 if total_fitness == 0 else fit / total_fitness for fit in fitnesses ]
    return random.choices(population=strings,weights=probabilities_of_reproduction,k=NUM_STRINGS)

def perform_mutations(list_of_strings):
    """
    Takes a list of strings, returns a list of potentially mutated binary strings

    Args:
        string: List of binary strings to mutate
    Returns:
        new_list_of_strings: List of potentially mutated binary strings
    """
    return [attempt_mutation(s) for s in list_of_strings]

def perform_mating(list_of_strings):
    """
    Takes a list of strings, returns a list of binary strings after crossover operation

    Args:
        list_of_strings: List of binary strings to mate
    Returns:
        new_list_of_strings: List of binary strings after crossover operation
    """
    new_list_of_strings = []

    while(len(list_of_strings) > 0):
        s1 = list_of_strings.pop(random.randint(0, len(list_of_strings)-1))
        s2 = list_of_strings.pop(random.randint(0, len(list_of_strings)-1))

        s1p, s2p = crossover_pair(s1, s2)
        new_list_of_strings.append(s1p)
        new_list_of_strings.append(s2p)

    return new_list_of_strings

def select_best(strings,string2fitness ):
    return max(strings, key=string2fitness)

def delete_worst(strings,string2fitness):
    minVal = min(strings, key=string2fitness)
    strings.remove(minVal)
    return strings

def attempt_mutation(s):
    """
    Takes a string to perform low probability bit mutation on

    Args:
        s: Binary string to mutate
    Returns:
        new_string: Mutated binary string
    """
   #bit flipping 
    if random.random() > PROBABILITY_OF_MUTATION:
       bit_to_flip = random.randint(0,len(s)-1)
       s = list(s)
       s[bit_to_flip] = random.choice(BIN_ALPHABET)
       return "".join(s)
    else:
        return s

def crossover_pair(s1, s2):
    """
    Takes two binary strings for crossover. Randomly selects a crossover point between 1 and len(s1)-1. 
    Performs crossover then returns mated binary string pair.
    Assumes len(s1) = len(s2)

    Args:
        s1: Binary string for mating crossover
        s2: Binary string for mating crossover
    Returns:
        s1p: Binary string from mating crossover
        s2p: Binary string from mating crossover
    """
    crossover_point = random.randint(1, len(s1)-2)

    s1p = s1[:crossover_point] + s2[crossover_point:]
    s2p = s2[:crossover_point] + s1[crossover_point:]

    return (s1p, s2p)


def initialize(num_strings:int, alphabet:List[str])-> List[str]:
    """
    Generates num_strings of random binary strings with characters in alphabet

    Args:
        num_strings: Number of string to be generated 
        alphabet: Valid characters
    Returns:
        List of num_strings random binary strings with characters in alphabet
    """

    return ["".join(random.choices(alphabet, k=STRING_LEN)) for _ in range(num_strings)]


def print_table(strings, test_func,fitness_func,decoder_func):
    """ 
    Takes in binary string mating pool and pretty prints each string's reproduction performance stats

    Args:
        strings: List of binary strings that makes up the mating pool
        test_func: Function used to test found fitness  ex: Himmelblau (1000 - 0) 
                    Results closer to zero are closer to optimization
        fitness_func: Compares fitness measure to benchmark of optimization  ex: Himmelblau (0 - 1000)
                    Higher values are higher fitness
        decoder_func: Used to decode binary strings into integers
    Prints:
        Table containing binary string; its performed fitness level with the test function; 
        (x, y) cartesian coordinates used as inputs for test function; result of measured fitness compared to benchmark value;
        and the likelihood that the string will reproduce, as a proportion of its fitness to the accumulated fitness of its mating pool.
    """
    total_fitness = sum([fitness_func(test_func(*decoder_func(s))) for s in strings])
    proportion = [0 if total_fitness == 0 else fitness_func(test_func(*decoder_func(s))) / total_fitness for s in strings ]

    print("{:11}{:11}{:11}{:11}{:>15}".format("String", "Fitness", "Coord", "Result", "Proportion of total"))
    print("="*65)
    for s,p in zip(strings,proportion):
        print("{:11s}{:<11}{}{:4}{:<11}{:>.15f}".format(s,fitness_func(test_func(*decoder_func(s))),decoder_func(s),"",test_func(*decoder_func(s)),p)) #TODO wasn't able to figure out how to format print a tuple with padding so that the last 2 columns would look consistent
    print("="*65)
    print("")


def objective(string, test_func, fitness_func,  decoder) -> int:
    return fitness_func(test_func(decoder(string)))


#program starts here:
#-------------------------------------------------------------------------------------------------------------------------------------------

#create initial mating pool
strings = initialize(NUM_STRINGS, BIN_ALPHABET)

#choose method for decoding binary strings
decode_func = decode_himmelblau

#choose fitness regimine TODO define operation
s2f = string2fitness(himmelblau,fitness_func,decode_func)

#TODO define operation
test_func = functionWithDomain(himmelblau)


for _ in range(NUM_GENERATIONS):
    strings = perform_reproduction(strings, s2f)
    
    best = select_best(strings,s2f)

    strings = perform_mating(strings)
    strings = perform_mutations(strings)

    strings = delete_worst(strings, s2f)+[best]

    print_table(strings, test_func, fitness_func, decode_func)