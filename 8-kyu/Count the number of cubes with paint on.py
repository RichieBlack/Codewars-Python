"""
@File    : Count the number of cubes with paint on.py 
@Author  : Richie Black
@Time    : 31.10.2022 18:59

I have been learning Python since August 2022.
"""


def count_squares(cuts):
    x = cuts + 1
    cubes = x ** 2
    all_cubes = cubes * x
    visible_cubes = all_cubes - ((x - 2) ** 2) * (x - 2)

    print(x, '#', cubes, '#', all_cubes, '#', visible_cubes)

    return visible_cubes


"""Best practices
-----------------

''' PROOF:
number of cuts = x
The total number of cubes = (x+1)^3
the number of all blue cubes = (x-1)^3

Number of cubes with one or more red squares:
= (x+1)^3 - (x-1)^3
= (x+1)(x+1)(x+1) - (x-1)(x-1)(x-1)
= x^3 + 3x^2 + 3x + 1 - (x^3 - 3x^2 + 3x -1 )
= 6x^2 + 2

'''

def count_squares(x):
    return 6 * x**2 + 2

-----------------

def count_squares(x):
    return  (x + 1) ** 3 - (x - 1) ** 3

-----------------

def count_squares(cuts):
    return 6 * cuts**2 + 2

-----------------
"""

# https://www.codewars.com/kata/reviews/5764f23c190b14d64a0015a4/groups/635060e7e2eb0500014922f2
