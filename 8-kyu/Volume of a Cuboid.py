"""
@File    : Volume of a Cuboid.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:50

I have been learning Python since August 2022.
"""


def get_volume_of_cuboid(length, width, height):
    return length * width * height


"""Best practices
-----------------

def get_volume_of_cuboid(length, width, height):
    return length * width * height

-----------------

from functools import reduce


def get_volume_of_cuboid(*args):
    return int(reduce(lambda x, y: x * y, args))

-----------------
"""

# https://www.codewars.com/kata/reviews/58262cce57bd30b5dd0000a4/groups/63283cf52a0c700001a67fd7
