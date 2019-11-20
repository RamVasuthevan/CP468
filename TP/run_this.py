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

#Takes in the list of all strings, and probabalistically selects a list of length len(list_of_strings) based on the relative fitness of each string
def perform_repoduction(strings, string2fitness) -> List:
    fitnesses = [ string2fitness(s) for s in strings]
    total_fitness = sum(fitnesses)
    probabilities_of_reproduction = [0 if total_fitness == 0 else fit / total_fitness for fit in fitnesses ]
    return random.choices(population=strings,weights=probabilities_of_reproduction,k=NUM_STRINGS)

#takes a list of strings, returns a list of potentially mutated strings
def perform_mutations(list_of_strings):
    return [attempt_mutation(s) for s in list_of_strings]

def perform_mating(list_of_strings):
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
   #bit flipping 
    if random.random() > PROBABILITY_OF_MUTATION:
       bit_to_flip = random.randint(0,len(s)-1)
       s = list(s)
       s[bit_to_flip] = random.choice(BIN_ALPHABET)
       return "".join(s)
    else:
        return s

# takes two strings for crossover. Randomly selects a crossover point between 1 and len(s1)-1. Performs crossover on and returns both new strings.
#assumes len(s1) = len(s2)
def crossover_pair(s1, s2):
    crossover_point = random.randint(1, len(s1)-2)

    s1p = s1[:crossover_point] + s2[crossover_point:]
    s2p = s2[:crossover_point] + s1[crossover_point:]

    return (s1p, s2p)


def initialize(num_strings:int, alphabet:List[str])-> List[str]:
    """
    Generates num_strings random strings with characters in alphabet
    Args:
        num_strings: Number of string to be generated 
        alphabet: Valid characters
    Returns:
        List of num_strings random strings with characters in alphabet
    """

    return ["".join(random.choices(alphabet, k=STRING_LEN)) for _ in range(num_strings)]


def print_table(strings, test_func,fitness_func,decoder_func):
    total_fitness = sum([fitness_func(test_func(*decoder_func(s))) for s in strings])
    proportion = [0 if total_fitness == 0 else fitness_func(test_func(*decoder_func(s))) / total_fitness for s in strings ]

    print("String \t\t Fitness \t Coord \t\t Result \t Proportion of total")
    print("="*100)
    for s,p in zip(strings,proportion):
        print("{} \t\t {} \t\t {} \t {} \t {}".format(s,fitness_func(test_func(*decoder_func(s))),decoder_func(s),test_func(*decoder_func(s)),p))
    print("="*100)
    print("")


def objective(string, test_func, fitness_func,  decoder) -> int:
    return fitness_func(test_func(decoder(string)))


#program starts here:
#-------------------------------------------------------------------------------------------------------------------------------------------

strings = initialize(NUM_STRINGS, BIN_ALPHABET)
decode_func = decode_himmelblau
s2f = string2fitness(himmelblau,fitness_func,decode_func)
test_func = functionWithDomain(himmelblau)


for _ in range(NUM_GENERATIONS):
    strings = perform_repoduction(strings, s2f)
    
    best = select_best(strings,s2f)

    strings = perform_mating(strings)
    strings = perform_mutations(strings)

    strings = delete_worst(strings, s2f)+[best]

    print_table(strings, test_func, fitness_func, decode_func)