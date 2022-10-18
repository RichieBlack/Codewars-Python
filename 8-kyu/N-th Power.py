# https://www.codewars.com/kata/reviews/57ef10fccfdb1a41ef00001b/groups/57f16f591b5432ae510002c2

def index(array, n):
    return -1 if len(array) <= n else array[n] ** n


# I have been studying Python for one month.

"""Best practices
-----------------

def index(array, n):
    try:
        return array[n]**n
    except:
        return -1

-----------------

def index(array, n):
    return array[n]**n if n < len(array) else -1

-----------------

def index(array, n):
    if n < len(array):
        return (array[n])**n
    else:
        return -1

-----------------
"""
