"""
@File    : Powers of 2.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:16

I have been learning Python since August 2022.
"""


def powers_of_two(n):
    return [2 ** i for i in range(0, n + 1)]


"""Best practices
-----------------

def powers_of_two(n):
    return [2 ** x for x in range(n + 1)]

-----------------

def powers_of_two(n):
    a = []
    for i in range(0, n + 1):
        a.append(2 ** i)    
    return a

-----------------

def powers_of_two(n):
    return [1 << x for x in range(n + 1)]


-----------------
"""

# https://www.codewars.com/kata/reviews/57a0fbac577a8db22700004e/groups/6328c85e6f58be00018ebe7a
