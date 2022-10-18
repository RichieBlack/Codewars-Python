# https://www.codewars.com/kata/reviews/5ab689a7e6a5d4b4e7000070/groups/5ab776281310f8ddb7001933

def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2


# I have been studying Python for one month.

"""Best practices
-----------------

def area_or_perimeter(l, w):
    return l * w if l == w else (l + w) * 2

-----------------

def area_or_perimeter(l , w):
    return l * w if l == w else 2 * (l + w)

-----------------

area_or_perimeter = lambda a, b : a * b if a == b else 2 * (a + b)

-----------------
"""
