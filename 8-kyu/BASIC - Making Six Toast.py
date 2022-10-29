"""
@File    : BASIC - Making Six Toast.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:49

I have been learning Python since August 2022.
"""


def six_toast(num):
    return abs(num - 6)


"""Best practices
-----------------

def six_toast(num):
    return abs(num - 6)

-----------------

six_toast = lambda n: abs(6 - n)

-----------------

def six_toast( n ):
    return n - 6 if n > 6 else 6 - n

-----------------
"""

# https://www.codewars.com/kata/reviews/583522cff6389d842c000020/groups/6342d9e642231700011ea626
