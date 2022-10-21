"""
@File    : Grasshopper - Terminal game move function.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:13

I have been learning Python since August 2022.
"""


def move(position, roll):
    return position + (roll * 2)


"""Best practices
-----------------

def move(position, roll):
    return position + 2 * roll

-----------------

move = lambda p, r: p + r * 2

-----------------

def move(position, roll):
    return position + (roll << 1)

-----------------
"""

# https://www.codewars.com/kata/reviews/5764a03d5274c658250011ef/groups/6328bc1d48be1500018fc306
