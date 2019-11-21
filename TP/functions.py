import sys
from math import log
from inspect import signature
from  textwrap import wrap

DOMAIN = 8
MAX_VAL = 1000

def himmelblau(x,y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

#String definition: binary representation of numbers less than 10 for x, then y, ie. 4 bits, repeated twice
#takes a string, and returns the x and y values in decimal
def decode_himmelblau(string):
    x_bin = string[:4]
    y_bin = string[4:]
    return signedBin2Dec(x_bin),signedBin2Dec(y_bin)

def gen_decoder_function(func):
    num_arg = len(signature(func).parameters.keys())
    def inner(string):
        return (signedBin2Dec(s) for s in wrap(string,num_arg))
    return inner

def signedBin2Dec(s):
    sign = int(s[0])
    if not sign:
        sign = -1
    return sign*int(s[1:],2)

def functionWithDomain(func):
    def inner(*args):
        if any(map(lambda x:x > DOMAIN, args)):
            return MAX_VAL
        else:
            return func(*args)
    return inner

def fitness_func(val):
    return max(MAX_VAL - val, 0)

def string2fitness(test_func,fitness_func,decoder_func):
    """#TODO update docstring
    Takes in mating pool of binary strings, and probabalistically selects a list of length, len(list_of_strings), 
    based on the relative fitness of each string

    Args:
        test_func: Function used to test found fitness  ex: Himmelblau (1000 - 0) 
                    Results closer to zero are closer to optimization
        fitness_func: Compares fitness measure to benchmark of optimization  ex: Himmelblau (0 - 1000)
                    Higher values are higher fitness
        decoder: Used to decode binary strings into integers
    Returns:
        new_generation_of_strings: List of binary strings
    """
    def inner(s:str)->int:
        return fitness_func(test_func(*decoder_func(s)))
    return inner
