"""
@File    : Are arrow functions odd.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:41

I have been learning Python since August 2022.
"""


def odds(arr):
    return [i for i in arr if i % 2]


"""Best practices
-----------------

def odds(values):
        return [i for i in values if i % 2]

-----------------

odds = lambda odd: [i for i in odd if i % 2 != 0]

-----------------

def odds(values):
    return list(filter((1).__rand__, values))

-----------------
"""

# https://www.codewars.com/kata/reviews/6001052add237e00014930f8/groups/6339f0fcc9198d0001d2ee93
