"""
@File    : Sort and Star.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:45

I have been learning Python since August 2022.
"""


def two_sort(array):
    array = sorted(array)
    first_word = list((array[0]))

    return ('***'.join(first_word))


"""Best practices
-----------------

def two_sort(lst):
    return '***'.join(min(lst))

-----------------

def two_sort(arr):
    return '***'.join(sorted(arr)[0])

-----------------

def two_sort(array):
    return '***'.join(min(array))

-----------------
"""

# https://www.codewars.com/kata/reviews/5af2a141f82f0221f70004c7/groups/63299a61f5f54000010c492d
