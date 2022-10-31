"""
@File    : Coefficients of the Quadratic Equation.py 
@Author  : Richie Black
@Time    : 31.10.2022 19:07

I have been learning Python since August 2022.
"""


def quadratic(x1, x2):
    return 1, (x1 + x2) * -1, x1 * x2


"""Best practices
-----------------

def quadratic(x1, x2):
    return (1, -x1 - x2, x1 * x2)

-----------------

def quadratic(x1, x2):
    return (1, -(x1 + x2), x1 * x2)

-----------------

import numpy as np


def quadratic(*args):
    return tuple(np.poly(args))

-----------------
"""

# https://www.codewars.com/kata/reviews/5d59576f68ba810001f1f8db/groups/6355496038d1380001e942c5
