"""
@File    : Filling an array (part 1).py 
@Author  : Richie Black
@Time    : 22.10.2022 21:09

I have been learning Python since August 2022.
"""


def arr(n=0):
    return [i for i in range(n)] if n else []


"""Best practices
-----------------

def arr(n=0): 
    return list(range(n))

-----------------

def arr(n=0): 
    return [i for i in range(n)]

-----------------

def arr(n=0): 
    return [*range(n)]

-----------------
"""

# https://www.codewars.com/kata/reviews/5f479bcabb992f000171d6f5/groups/632aa662684b740001863415
