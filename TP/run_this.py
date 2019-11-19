from typing import Tuple, List, Dict
import random
import sys

PROBABILITY_OF_MUTATION = 0.001
STRING_LEN = 8 #for himmelblau
ALPHABET = ["0","1"] #TODO change this to the correct values of the alphabet
NUM_STRINGS = 10 #TODO change this to a constant of our choice, should be an even number (for mating)
NUM_GENERATIONS = 2

#Takes in the list of all strings, and probabalistically selects a list of length len(list_of_strings) based on the relative fitness of each string
def reproduction(list_of_strings, test_func, decoder) -> List:
    new_generation_of_strings = []
    probabilities_of_reproduction = []
    fitnesses = []
    total_fitness = 0

    for i in range(len(list_of_strings)):
        fitness = objective(list_of_strings[i], test_func, decoder)
        fitnesses.append(fitness)
        total_fitness += fitness
    
    print_table(list_of_strings, fitnesses, total_fitness)

    for i in range(len(fitnesses)):
        probabilities_of_reproduction.append(fitnesses[i] / total_fitness)

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
def perform_mustations(list_of_strings):
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

def initialize(num_strings: int, alphabet: list) -> list:
    list_of_strings = []

    for _ in range(num_strings):
        new_string = ""
        for _ in range(STRING_LEN):
            new_string += alphabet[random.randint(0,len(alphabet)-1)]
        list_of_strings.append(new_string)
    return list_of_strings


def print_table(strings, fitnesses, total_fitness):
    print("String # \t String \t\t Fitness \t\t\t % of total")
    print("====================================================================================================")
    for i in range(len(strings)):
        print("{} \t\t {} \t\t {} \t\t {}".format(i,strings[i],fitnesses[i],fitnesses[i]/total_fitness))
    print("====================================================================================================")
    print("Total \t\t\t\t\t {} \t\t {}".format(total_fitness, "100.0"))


def objective(string, test_func, decoder) -> int:
    return test_func(decoder(string)) 

#domain: -5.12 < x_i < 5.12
def DeJongSphere(x):
    return #TODO

#String definition: binary representation of numbers less than 10 for x, then y, ie. 4 bits, repeated twice
#takes a string, and returns the x and y values in decimal
def decode_himmelblau(string):
    x_bin = string[:4]
    y_bin = string[4:]
    # print("x_bin",x_bin)
    # print("y_bin",y_bin)
    x_dec = 0
    y_dec = 0
    for i in range(3,0, -1):
        x_dec += int(x_bin[i]) * 2 ** (3-i)
        y_dec += int(y_bin[i]) * 2 ** (3-i)
    
    # print("x_dec",x_dec)
    # print("y_dec",y_dec)
    
    return (x_dec - 5, y_dec -5)

#domain: -5 < x,y < 5
# if x,y not in domain, returns sys.maxsize
def himmelblau(xy):
    x,y = xy
    # print("x:",x," y:",y)
    if(not -5 < x < 5 or not -5 < y < 5):
        return sys.maxsize
    
    return (x**2 + y -11)**2 + (x + y**2 -7)**2




#program starts here:
#-------------------------------------------------------------------------------------------------------------------------------------------

strings = initialize(NUM_STRINGS, ALPHABET)

for _ in range(NUM_GENERATIONS):
    strings = reproduction(strings, himmelblau, decode_himmelblau)
    strings = perform_mating(strings)
    strings = perform_mustations(strings)