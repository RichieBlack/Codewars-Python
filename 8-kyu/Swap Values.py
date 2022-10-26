"""
@File    : Swap Values.py 
@Author  : Richie Black
@Time    : 26.10.2022 20:46

I have been learning Python since August 2022.
"""


def swap_values(args):
    args[0], args[1] = args[1], args[0]
    return args


"""Best practices
-----------------

def swap_values(args): 
    args[0], args[1] = args[1], args[0]
    return args

-----------------

swap_values = list.reverse

-----------------

def swap_values(arr): 
    arr.reverse()

-----------------
"""

# https://www.codewars.com/kata/reviews/5db0c040e8cc470001a5811e/groups/632de479ee1c3f00017f501e