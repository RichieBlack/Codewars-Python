"""
@File    : Area of a Square.py 
@Author  : Richie Black
@Time    : 27.10.2022 13:49

I have been learning Python since August 2022.
"""

import math


def square_area(A):
    return round((A * 4 / math.pi * 2) ** 2, 2)


"""Best practices
-----------------

from math import pi


def square_area(A):
    return round((2 * A / pi) ** 2, 2)

-----------------

import math


def square_area(A):
    return round((A * 4 / (2 * math.pi)) ** 2, 2)

-----------------

square_area = lambda A: round((4 * A / __import__("math").pi / 2) ** 2, 2)

-----------------
"""

# https://www.codewars.com/kata/reviews/5dc4e7e4b9b5a2000185f694/groups/6330aad595410400014c9ffa
