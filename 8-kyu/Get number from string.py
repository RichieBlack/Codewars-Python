"""
@File    : Get number from string.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:25

I have been learning Python since August 2022.
"""


def get_number_from_string(string):
    """Write a function which removes from string all non-digit characters
    and parse the remaining to number.

    E.g: "hell5o wor6ld" -> 56
    """
    parse = ''
    for n in range(len(string)):
        if string[n].isdigit():
            parse += string[n]
    return int(parse)


"""Best practices
-----------------

def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))

-----------------

import re


def get_number_from_string(s):
    return int(re.sub(r'\D', '', s))

-----------------

def get_number_from_string(s):
    return int(filter(str.isdigit, s))

-----------------
"""

# https://www.codewars.com/kata/reviews/57a602b511c323abb0000070/groups/634d940f9dbacb00012f721f
