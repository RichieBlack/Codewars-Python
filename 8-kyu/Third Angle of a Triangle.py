"""
@File    : Third Angle of a Triangle.py 
@Author  : Richie Black
@Time    : 20.10.2022 21:03

I have been learning Python since August 2022.
"""


def other_angle(a, b):
    return 180 - a - b


"""Best practices
-----------------

def other_angle(a, b):
    return 180 - a - b

-----------------

def other_angle(a, b):
    if (a or b) < 0:
        return "angle cannot be smaller than 0"
    
    else:
        return 180 - (a + b)

-----------------

other_angle = lambda a, b: 180 - (a + b)

-----------------
"""

# https://www.codewars.com/kata/reviews/5a023dd23d6570d29f003b60/groups/632846caa9ebca0001d3378b
