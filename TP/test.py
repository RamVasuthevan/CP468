from inspect import signature
def f(a,b,c):
    return a+b+c

x = len(signature(f).parameters.keys())

True