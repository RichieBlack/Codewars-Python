"""
@File    : Find the position.py 
@Author  : Richie Black
@Time    : 27.10.2022 7:27

I have been learning Python since August 2022.
"""


def position(alphabet):
    a = 'abcdefghijklmnopqrstuvwxyz'
    return f'Position of alphabet: {a.find(alphabet) + 1}'


"""Best practices
-----------------

def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)


-----------------

def position(alphabet):
    return "Position of alphabet: %s" % ("abcdefghijklmnopqrstuvwxyz".find(alphabet) + 1)

-----------------

from string import ascii_lowercase


def position(char):
    return "Position of alphabet: {0}".format(ascii_lowercase.index(char) + 1)

-----------------
"""

# https://www.codewars.com/kata/reviews/580928f6d6bd8d2bfe00006e/groups/6330866195410400014c9756
