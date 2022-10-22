"""
@File    : Stringy Strings.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:40

I have been learning Python since August 2022.
"""


def stringy(size):
    bin = ''

    for i in range(size):
        if i % 2:
            bin = bin + '0'
        else:
            bin = bin + '1'
    return bin


"""Best practices
-----------------

def stringy(size):
    return "".join([str(i % 2) for i in range(1, size + 1)])

-----------------

def stringy(size):
    return ('10' * size)[:size]

-----------------

def stringy(size):
    return '10' * (size // 2) + '1' * (size % 2)

-----------------

from itertools import cycle, islice


def stringy(size):
    return ''.join(islice(cycle('10'), size))
    
-----------------
"""

# https://www.codewars.com/kata/reviews/563c67603f4d5d110300000f/groups/6329d06fa838690001735fb6
