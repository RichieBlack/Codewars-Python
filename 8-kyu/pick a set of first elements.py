"""
@File    : pick a set of first elements.py 
@Author  : Richie Black
@Time    : 31.10.2022 19:15

I have been learning Python since August 2022.
"""


def first(seq, n=1):
    return seq[:n] if 0 < n else []


"""Best practices
-----------------

def first(seq, n=1): 
    return seq[:n]

-----------------

def first(seq, n=None): 
    return  seq[:n] if n != None else [seq[0]]

-----------------

first = lambda a, i=1: a[:i]

-----------------
"""

# https://www.codewars.com/kata/reviews/6075f3d3b0cc8b0001d9081c/groups/635aad69081f2c0001bbd305
