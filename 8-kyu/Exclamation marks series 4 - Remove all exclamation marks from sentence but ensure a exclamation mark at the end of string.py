"""
@File    : Exclamation marks series 4 - Remove all exclamation marks from sentence
           but ensure a exclamation mark at the end of string.py
@Author  : Richie Black
@Time    : 29.10.2022 1:00

I have been learning Python since August 2022.
"""


def remove(s):
    return s.replace('!', '') + '!'


"""Best practices
-----------------

def remove(s):
    return s.replace("!", "") + "!"

-----------------

def remove(s):
    return '{}!'.format(s.replace('!', ''))

-----------------

remove = lambda s: s.replace('!', '') + '!'

-----------------
"""

# https://www.codewars.com/kata/reviews/58017f38da4d7ecf9b00001b/groups/633df658ab2f580001cfe0cf
