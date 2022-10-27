"""
@File    : Printing Array elements with Comma delimiters.py 
@Author  : Richie Black
@Time    : 27.10.2022 6:53

I have been learning Python since August 2022.
"""


def print_array(arr):
    return ','.join(map(str, arr))


"""Best practices
-----------------

def print_array(arr):
    return ','.join(map(str, arr))

-----------------

def print_array(arr):
    return ','.join(str(a) for a in arr)

-----------------

print_array = lambda a: ','.join(map(str, a))

-----------------
"""

# https://www.codewars.com/kata/reviews/5717a12a7a3423e6a000000a/groups/632f62c956e8d300012fbd05
