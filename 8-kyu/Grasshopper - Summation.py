# https://www.codewars.com/kata/reviews/55edaf822eb94fbfe60001a5/groups/55f2d3bd76edcf5b5c000040

def summation(num):
    sum = 0
    for i in range(0, num + 1):
        sum += i
    return sum


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def summation(num):
    return sum(xrange(num + 1))

---------------

def summation(num):
    return (1 + num) * num / 2

---------------

def summation(num):
    return sum(range(1, num + 1))

---------------

summation = lambda n: n*-~n>>1

---------------
"""
