"""
@File    : Who is going to pay for the wall.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:17

I have been learning Python since August 2022.
"""


def who_is_paying(name):
    if len(name) > 2:
        return [name, name[0:2]]
    else:
        return [name]


"""Best practices
-----------------

def who_is_paying(name):
    return [name, name[0:2]] if len(name) > 2 else [name]

-----------------

who_is_paying = lambda n: [n, n[:2]] if len(n) > 2 else [n]

-----------------

def who_is_paying(name):
    if len(name) > 2:
        return [name, name[0:2]]
    else:
        return [name[0:len(name)]]

-----------------

def who_is_paying(name):
    return [name] if len(name) <= 2 else [name, name[:2]]
    
-----------------
"""

# https://www.codewars.com/kata/reviews/5958bf1d44e3fd32b2000491/groups/63432df32575f00001cf2b00
