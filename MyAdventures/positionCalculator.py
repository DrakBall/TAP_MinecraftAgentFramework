from functools import reduce
from random import randint

def square_position(position):
    return list(map(lambda x: x**2, position))


def compose_functions(f, g):           #this funtion composes two functions
    return lambda x: f(g(x))             # functions will aply to the same argument


def random_multiplicator(x):
    return x*randint(1, 4)

def random_increment(x):
    return x+randint(1, 4)



if __name__=='__main__':
    print(compose_functions(random_multiplicator, random_increment)(70))  # Output: 30
    print(square_position([20,120,30]))