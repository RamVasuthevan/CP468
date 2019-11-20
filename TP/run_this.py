from typing import Tuple, List, Dict
import random
import sys
from functions import himmelblau, himmelblau_fitness, decode_himmelblau

PROBABILITY_OF_MUTATION = 0.001
STRING_LEN = 8 #for himmelblau
ALPHABET = ["0","1"] #TODO change this to the correct values of the alphabet
NUM_STRINGS = 10 #TODO change this to a constant of our choice, should be an even number (for mating)
NUM_GENERATIONS = 20

#Takes in the list of all strings, and probabalistically selects a list of length len(list_of_strings) based on the relative fitness of each string
def reproduction(list_of_strings:List[str], test_func, fitness_func, decoder) -> List:
    new_generation_of_strings = []
    probabilities_of_reproduction = []

    fitnesses = [objective(string, test_func, fitness_func, decoder) for string in list_of_strings]
    total_fitness = sum(fitnesses)

    print_table(list_of_strings, fitnesses, total_fitness,test_func,decoder)

    probabilities_of_reproduction = [0 if total_fitness == 1 else fit / total_fitness for fit in fitnesses ]

    for _ in range(NUM_STRINGS):
        rand = random.random() #a number in [0.0, 1.0)

        bottom = 0
        top = probabilities_of_reproduction[0]
        i = 0
        while not bottom < rand <= top:
            i += 1
            bottom = top
            top = probabilities_of_reproduction[i] + top
        # i should now be the index of the string selected to reproduce

        new_generation_of_strings.append(list_of_strings[i])
    
    return new_generation_of_strings

# takes two strings for crossover. Randomly selects a crossover point between 1 and len(s1)-1. Performs crossover on and returns both new strings.
#assumes len(s1) = len(s2)
def crossover_pair(s1, s2):
    crossover_point = random.randint(1, len(s1)-2)

    s1p = s1[:crossover_point] + s2[crossover_point:]
    s2p = s2[:crossover_point] + s1[crossover_point:]

    return (s1p, s2p)

def attempt_mutation(string):
    new_string = ""
    for i in range(len(string)):
        rand = random.random()
        if(rand < PROBABILITY_OF_MUTATION): #then mutate
            new_string += ALPHABET[random.randint(0, len(ALPHABET)-1)] #TODO see if we need to exclude the previous value of string[i] when ewe mutate
        else:
            new_string += string[i]

    return new_string

#takes a list of strings, returns a list of potentially mutated strings
def perform_mutations(list_of_strings):
    new_list_of_strings = []
    for string in list_of_strings:
        new_list_of_strings.append(attempt_mutation(string))
    return new_list_of_strings



def perform_mating(list_of_strings):
    new_list_of_strings = []

    while(len(list_of_strings) > 0):
        s1 = list_of_strings.pop(random.randint(0, len(list_of_strings)-1))
        s2 = list_of_strings.pop(random.randint(0, len(list_of_strings)-1))

        s1p, s2p = crossover_pair(s1, s2)
        new_list_of_strings.append(s1p)
        new_list_of_strings.append(s2p)

    return new_list_of_strings

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


def print_table(strings, fitnesses, total_fitness,func, decoder):
    print("String # \t String \t\t Fitness \t Coord \t\t Result \t Proportion of total")
    print("====================================================================================================")
    for i in range(len(strings)):
        print("{} \t\t {} \t\t {} \t {} \t {} \t {}".format(i,strings[i],fitnesses[i],decoder(strings[i]), func(decoder(strings[i])) ,0 if total_fitness == 0 else fitnesses[i]/total_fitness))
    print("====================================================================================================")
    print("Total \t\t\t\t\t {} \t\t {}".format(total_fitness, "1"))
    print("")


def objective(string, test_func, fitness_func,  decoder) -> int:
    return fitness_func(test_func(decoder(string)))





#program starts here:
#-------------------------------------------------------------------------------------------------------------------------------------------


strings = initialize(NUM_STRINGS, ALPHABET)

for _ in range(NUM_GENERATIONS):
    strings = reproduction(strings, himmelblau,himmelblau_fitness, decode_himmelblau)
    strings = perform_mating(strings)
    strings = perform_mutations(strings)

print(himmelblau((3,2)))