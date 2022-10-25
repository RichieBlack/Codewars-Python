"""
@File    : Super Duper Easy.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:37

I have been learning Python since August 2022.
"""


def problem(a):
    try:
        return a * 50 + 6
    except:
        return "Error"


"""Best practices
-----------------

def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"

-----------------

def problem(a):
    return "Error" if isinstance(a, str) else a * 50 + 6

-----------------

def problem(a):
    if isinstance(a, str):
        return "Error"
    else:
        return (a * 50) + 6

-----------------
"""

# https://www.codewars.com/kata/reviews/55a5bfb95c754688c0000219/groups/632dc7e85f07700001c97c97
