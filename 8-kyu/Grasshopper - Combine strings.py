"""
@File    : Grasshopper - Combine strings.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:10

I have been learning Python since August 2022.
"""


def combine_names(first_name, last_name):
    return f'{first_name} {last_name}'


"""Best practices
-----------------

def combine_names(first, last):
    return first + " " + last

-----------------

def combine_names(*args):
    return ' '.join(args)

-----------------

def combine_names(first, second):
    return '{} {}'.format(first, second)

-----------------
"""

# https://www.codewars.com/kata/reviews/5633f10cfb3281ba19000025/groups/6336e485cd12d200019fe300
