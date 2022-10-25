"""
@File    : Generate range of integers.py 
@Author  : Richie Black
@Time    : 25.10.2022 18:52

I have been learning Python since August 2022.
"""


def generate_range(min, max, step):
    return [n for n in range(min, max + 1, step)]


"""Best practices
-----------------

def generate_range(min, max, step):
    return list(range(min, max + 1, step))

-----------------

def generate_range(min, max, step):
    return [i for i in range(min, max + 1, step)]

-----------------

generate_range = lambda a, b, c: list(range(a, b+1, c))

-----------------
"""

# https://www.codewars.com/kata/reviews/60680e2b6ce1ce0001cc20b1/groups/632c64fd07a561000136b075
