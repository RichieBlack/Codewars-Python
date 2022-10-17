# https://www.codewars.com/kata/reviews/5a45529df50c11633000068c/groups/6321d6e91c3908000106eb4e

def odd_count(n):
    return round(n//2) if n % 2 != 0 else n/2


# I have been studying Python for one month.

"""Best practices
-----------------

def oddCount(n):
    return n // 2

-----------------

def odd_count(n):
    return len(range(1, n, 2))

-----------------

def odd_count(n): return n >> 1

-----------------
"""