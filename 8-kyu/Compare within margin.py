"""
@File    : Compare within margin.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:38

I have been learning Python since August 2022.
"""


def close_compare(a, b, margin=0):
    return 0 if abs(a - b) <= margin else - 1 if b > a else 1


"""Best practices
-----------------

def close_compare(a, b, margin = 0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1

-----------------

def close_compare(a, b, margin=0):
    if a == b or abs(a - b) <= margin:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1

-----------------

from numpy import sign

def close_compare(a, b, margin=0):
    return abs(a-b) > margin and sign(a-b)

-----------------

close_compare = lambda a, b, m=0: 0 if abs(a - b) <= m else -1 * (a < b) + (a > b)

-----------------
"""

# https://www.codewars.com/kata/reviews/57bd9e79e3ebb72d02000032/groups/6339ec96815ea300014ae3d0
