"""
@File    : Geometry Basics - Distance between points in 2D.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:19

I have been learning Python since August 2022.
"""


def distance_between_points(a, b):
    """"Write a function calculating distance between Point a and Point b.

    Tests round answers to 6 decimal places.
    """
    result = ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    if result - int(result) == 0:
        return (int(result))
    else:
        return (round(result, 6))


"""Best practices
-----------------

from math import hypot


def distance_between_points(a, b):
    return hypot(a.x - b.x, a.y - b.y)

-----------------

def distance_between_points(a, b):
    return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5

-----------------

import math


def distance_between_points(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

-----------------
"""
# https://www.codewars.com/kata/reviews/58dd9a568d29b0176f0002d5/groups/634c5ebf675bc30001fc41c7
