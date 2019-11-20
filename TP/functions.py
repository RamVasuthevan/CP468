import sys
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
    maxVal = 2**16-1
    if(not -maxVal < x < maxVal or not -maxVal < y < maxVal):
        return 1000

    return (x**2 + y -11)**2 + (x + y**2 -7)**2

def himmelblau_fitness(val):
    return 1000-val