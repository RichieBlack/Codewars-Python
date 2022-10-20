"""
@File    : Grasshopper - Check for factor.py 
@Author  : Richie Black
@Time    : 20.10.2022 21:40

I have been learning Python since August 2022.
"""


def check_for_factor(base, factor):
    return base % factor == 0


"""Best practices
-----------------

def check_for_factor(base, factor):
    return base % factor == 0

-----------------

def check_for_factor(b, f):
    return not b % f

-----------------

def check_for_factor(base, factor):
    return True if base % factor == 0 else False

-----------------
"""

# https://www.codewars.com/kata/reviews/5d78cd8ca4b23f0001b6cb9a/groups/63284c3fc032e000019b9eb6
