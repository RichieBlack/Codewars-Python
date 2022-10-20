"""
@File    : Find the first non-consecutive number.py 
@Author  : Richie Black
@Time    : 20.10.2022 3:58

I have been learning Python since August 2022.
"""


def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if i != j:
            return j


"""Best practices
-----------------

def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]

-----------------

def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None

-----------------

def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]

-----------------
"""

# https://www.codewars.com/kata/reviews/58fc84f949f5af674e0009f2/groups/6325c897c7d96000015b3008
