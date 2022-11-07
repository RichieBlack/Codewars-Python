"""
@File    : Smallest value of an array.py 
@Author  : Richie Black
@Time    : 08.11.2022 1:00

I have been learning Python since August 2022.
"""


def find_smallest(numbers, to_return):
    if to_return == "value":
        return min(numbers)

    elif to_return == "index":
        return numbers.index(min(numbers))


"""Best practices
-----------------

def find_smallest(numbers,to_return):
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))

-----------------

def find_smallest(numbers,to_return):
    val = min(numbers)
    return val if to_return == "value" else numbers.index(val)

-----------------

import numpy as np


def find_smallest(numbers, to_return):
    return (np.min, np.argmin)[to_return == 'index'](numbers)

-----------------

find_smallest = lambda n, t: [n.index, lambda x: x][t[0] == 'v'](min(n))

-----------------
"""

# https://www.codewars.com/kata/reviews/5990b3b635fd2f1876000047/groups/63697254d0b203000195cc65