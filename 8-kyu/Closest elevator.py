"""
@File    : Closest elevator.py 
@Author  : Richie Black
@Time    : 29.10.2022 0:45

I have been learning Python since August 2022.
"""


def elevator(left, right, call):
    if abs(call - left) < abs(call - right):
        return "left"
    else:
        return "right"


"""Best practices
-----------------

def elevator(left, right, call):
    return "left" if abs(call - left) < abs(call - right) else "right"

-----------------

def elevator(left, right, call):
    if abs(left - call) >= abs(right - call):
        return "right"
    else:
        return "left"

-----------------

elevator = lambda l, r, c: 'rliegfhtt'[abs(c - l) < abs(c - r)::2]

-----------------
"""

# https://www.codewars.com/kata/reviews/5c4cd2be8b87ad0001938798/groups/633b55ec61a8dc0001930a6c
