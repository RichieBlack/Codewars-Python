"""
@File    : Is it even.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:44

I have been learning Python since August 2022.
"""


def is_even(n):
    return not n % 2 == 0


"""Best practices
-----------------

def is_even(n): 
    return n % 2 == 0

-----------------

def is_even(n):  
    if (n % 2) == 1:
      return False
    elif (n % 2) == 0:
      return True 
    elif (n) != int: 
      return False 

-----------------

is_even = lambda n: n % 2 == 0

-----------------
"""
# https://www.codewars.com/kata/reviews/5e7f3ea5be09b60001b287c0/groups/632784ae921e140001ab6146
