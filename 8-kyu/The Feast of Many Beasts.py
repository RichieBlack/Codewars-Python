"""
@File    : The Feast of Many Beasts.py 
@Author  : Richie Black
@Time    : 20.10.2022 4:00

I have been learning Python since August 2022.
"""


def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


"""Best practices
-----------------

def feast(beast, dish):
    return beast[0] == dish[0] and dish[-1] == beast[-1]

-----------------

def feast(beast, dish):
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])

-----------------

def feast(b, d):
    return b[::len(b)-1] == d[::len(d)-1]

-----------------
"""

# https://www.codewars.com/kata/reviews/5ac0d1c252073ffdbf00092a/groups/6325eca6faa0b60001e2cda7
