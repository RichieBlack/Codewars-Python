"""
@File    : Find the Remainder.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:32

I have been learning Python since August 2022.
"""


def remainder(a, b):
    if a < b and a != 0:
        c = b % a
    elif a == 0 and b < 0:
        c = 0
    elif a == 0 or b == 0:
        c = None
    else:
        c = a % b
    return c


"""Best practices
-----------------

def remainder(a, b):
    if min(a, b) == 0:
        return None
    elif a > b:
        return a % b
    else: 
        return b % a

-----------------

def remainder(a,b):
    if min(a, b) != 0: 
        return max(a, b) % min(a, b)

-----------------

def remainder(a,b):
    return max(a, b) % min(a, b) if min(a, b) else None

-----------------
"""

# https://www.codewars.com/kata/reviews/61abbd07a811820001944936/groups/632db391bea9b500010e6ee1
