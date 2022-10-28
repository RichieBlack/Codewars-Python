"""
@File    : Find Nearest square number.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:35

I have been learning Python since August 2022.
"""


def nearest_sq(n):
    return round(n ** 0.5) ** 2


"""Best practices
-----------------

def nearest_sq(n):
    return round(n ** 0.5) ** 2

-----------------

from math import sqrt


def nearest_sq(n):
    return pow(round(sqrt(n)), 2)

-----------------

l, nearest_sq = lambda n: n * n,lambda n: l(round(n ** .5))

-----------------
"""

# https://www.codewars.com/kata/reviews/5a805d96afa10f8b930005bc/groups/633765437a672700013a3cef
