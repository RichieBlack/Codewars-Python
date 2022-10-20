"""
@File    : Difference of Volumes of Cuboids.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:59

I have been learning Python since August 2022.
"""


def find_difference(a, b):
    vol1 = a[0] * a[1] * a[2]
    vol2 = b[0] * b[1] * b[2]
    return abs(vol1 - vol2)


"""Best practices
-----------------

from numpy import prod


def find_difference(a, b):
    return abs(prod(a) - prod(b))

-----------------

def find_difference(a, b):
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])

-----------------

from operator import mul
from functools import reduce


def find_difference(a, b):
    return abs(reduce(mul, a) - reduce(mul, b))

-----------------
"""

# https://www.codewars.com/kata/reviews/58cb43f8256836ed95000f99/groups/632845e96f58be00018e9a68
