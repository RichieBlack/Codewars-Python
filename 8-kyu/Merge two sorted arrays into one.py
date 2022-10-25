"""
@File    : Merge two sorted arrays into one.py 
@Author  : Richie Black
@Time    : 25.10.2022 12:50

I have been learning Python since August 2022.
"""


def merge_arrays(arr1, arr2):
    arr3 = arr1 + arr2
    arr_set = set(arr3)
    arr_list = list(arr_set)
    arr_list.sort()
    return arr_list


"""Best practices
-----------------

def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

-----------------

def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1 + arr2)))

-----------------

merge_arrays = lambda a, b: sorted(list(set(a + b)))

-----------------
"""

# https://www.codewars.com/kata/reviews/589b9bed66413d26e4000033/groups/632b7309f8e278000157fc00
