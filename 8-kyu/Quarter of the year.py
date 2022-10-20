"""
@File    : Quarter of the year.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:20

I have been learning Python since August 2022.
"""


def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    elif month <= 12:
        return 4
    else:
        return None


"""Best practices
-----------------

def quarter_of(month):
    # your code here
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4

-----------------

from math import ceil


def quarter_of(month):
    return ceil(month / 3)

-----------------

def quarter_of(month):
    return (month + 2) // 3

-----------------
"""

# https://www.codewars.com/kata/reviews/5d0000ec2ad465000116bd8a/groups/6326021ffaa0b60001e2d26b
