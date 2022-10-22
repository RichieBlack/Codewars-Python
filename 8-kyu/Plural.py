"""
@File    : Plural.py 
@Author  : Richie Black
@Time    : 22.10.2022 21:14

I have been learning Python since August 2022.
"""


def plural(n):
    return n != 1


"""Best practices
-----------------

def plural(n):
    return n != 1

-----------------

def plural(n):
    return [True, False][n == 1]

-----------------

def plural(n):
    return False if n == 1 else True

-----------------
"""

# https://www.codewars.com/kata/reviews/556e07b47c58dac0c9000360/groups/632ad4a37c9f510001c08950
