"""
@File    : Merging sorted integer arrays (without duplicates).py 
@Author  : Richie Black
@Time    : 03.12.2022 19:17

I have been learning Python since August 2022.
"""


def merge_arrays(first, second):
    return sorted(set(first + second))


"""Best practices
-----------------

def merge_arrays(first, second): 
    return sorted(set(first + second))

-----------------

def merge_arrays(first, second): 
    working = []
    for e in first:
        if e not in working:
            working.append(e)
    for i in second:
        if i not in working:
            working.append(i)
    return sorted(working)

-----------------

def merge_arrays(first, second): 
    first.extend(second)
    x = list(set(first))
    x.sort()
    return x

-----------------
"""

# https://www.codewars.com/kata/reviews/5dc8198da613a800013fb8a8/groups/638b67f9bfaf7d000125afb4
