"""
@File    : Find out whether the shape is a cube.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:52

I have been learning Python since August 2022.
"""


def cube_checker(volume, side):
    return False if side <= 0 else side ** 3 == volume


"""Best practices
-----------------

def cube_checker(volume, side):
    return 0 < volume == side ** 3

-----------------

def cube_checker(volume, side):
    return side > 0 and side ** 3 == volume

-----------------

cube_checker = lambda v, s: v == s ** 3 > 0

-----------------
"""

# https://www.codewars.com/kata/reviews/5a13bbc6e8b13d5130000ea9/groups/6344bee4232728000164a6ce
