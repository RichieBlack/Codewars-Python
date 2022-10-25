"""
@File    : Array.diff.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:44

I have been learning Python since August 2022.
"""


def array_diff(a, b):
    return [i for i in a if i not in b]


"""Best practices
-----------------

def array_diff(a, b):
    return [x for x in a if x not in b]

-----------------

def array_diff(a, b):
    return [x for x in a if x not in set(b)]

-----------------

def array_diff(a, b):
    return filter(lambda i: i not in b, a)

-----------------

def array_diff(a, b):
    for n in b:
        while(n in a):
            a.remove(n)
    return a
    
-----------------
"""

# https://www.codewars.com/kata/reviews/5520ac91933cd0a1560002d2/groups/635807b2c385270001109dbe
