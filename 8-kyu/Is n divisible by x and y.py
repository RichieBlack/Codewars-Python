# https://www.codewars.com/kata/reviews/5589fda1a0db8600f9000064/groups/558a6ebaa4a715ced00000b3

def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


# I have been studying Python for one month.

"""Best practices
-----------------

def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

-----------------

def is_divisible(n, x, y):
    return n % x == n % y == 0

-----------------

def is_divisible(n, x, y):
    return not n % x and not n % y

-----------------
"""
