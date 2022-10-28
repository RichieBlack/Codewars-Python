"""
@File    : Pillars.py 
@Author  : Richie Black
@Time    : 28.10.2022 12:42

I have been learning Python since August 2022.
"""


def pillars(num_pill, dist, width):
    return ((num_pill - 1) * (dist * 100 + width) - width) if num_pill > 1 else 0


"""Best practices
-----------------

def pillars(num_pill, dist, width):
    return dist * 100 * (num_pill - 1) + width * (num_pill - 2) * (num_pill > 1)

-----------------

def pillars(n, dist, width):
    return (n - 1) * dist * 100 + max(n - 2, 0) * width

-----------------

def pillars(num_pill, dist, width):
    if num_pill <= 1:
        return 0
    else:
        return (num_pill - 2) * width + (num_pill - 1) * dist * 100

-------------

# https://www.codewars.com/kata/reviews/5bb0c5a5484fcd1707000642/groups/6334b2c2ebcadc0001e2cd4b
