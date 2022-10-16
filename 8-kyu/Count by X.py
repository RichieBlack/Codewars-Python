# https://www.codewars.com/kata/reviews/551609a119aab6c5240000b5/groups/63207a474de4f60001edd8f1

def count_by(x, n):
    seq = []
    seq = list(range(x, n * x + 1, x))
    return seq


# I have been studying Python for one month.

"""Best practices
-----------------

def count_by(x, n):
    return range(x, x * n + 1, x)

-----------------

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

-----------------

def count_by(x, n):
    arr = []
    for num in range(1, n + 1):
        result = x * num
        arr.append(result)
    return arr

-----------------
"""
