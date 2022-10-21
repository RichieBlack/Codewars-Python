"""
@File    : My head is at the wrong end.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:28

I have been learning Python since August 2022.
"""


def fix_the_meerkat(arr):
    return arr[::-1]


"""Best practices
-----------------

def fix_the_meerkat(arr):
    return arr[::-1]

-----------------

def fix_the_meerkat(arr):
    arr.reverse()
    return arr

-----------------

fix_the_meerkat = lambda a: a[::-1]

-----------------
"""

# https://www.codewars.com/kata/reviews/56f7d4696dfecaa2bc0000a4/groups/6328ee3736eabe00014b3789