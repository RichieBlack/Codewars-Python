"""
@File    : Enumerable Magic - Does My List Include This.py 
@Author  : Richie Black
@Time    : 27.10.2022 13:53

I have been learning Python since August 2022.
"""


def include(arr, item):
    return item in arr


"""Best practices
-----------------

def include(arr,item):
    return item in arr

-----------------

include = list.__contains__

-----------------

from operator import contains as include

-----------------

include = lambda a, i: i in a

-----------------
"""

# https://www.codewars.com/kata/reviews/5bc4d3d640ecc7c27b000680/groups/6330b342640f2100011d1ef0
