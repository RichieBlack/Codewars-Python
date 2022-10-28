"""
@File    : Add Length.py 
@Author  : Richie Black
@Time    : 28.10.2022 12:39

I have been learning Python since August 2022.
"""


def add_length(string):
    return [f'{i} {len(i)}' for i in string.split()]


"""Best practices
-----------------

def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]

-----------------

def add_length(str_):
    return [f"{w} {len(w)}" for w in str_.split()]

-----------------

def add_length(s):
    return ['%s %d' % (x, len(x)) for x in s.split()]

-------------

# https://www.codewars.com/kata/reviews/55a2609eefe76613e1000031/groups/63347c24cca62a0001603e14
