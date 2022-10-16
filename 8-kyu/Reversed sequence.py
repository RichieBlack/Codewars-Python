# https://www.codewars.com/kata/reviews/5a00e3810df25e625700255e/groups/5b05363cbbb2702363000dbc

def reverse_seq(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr[::-1]


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def reverseseq(n):
    return list(range(n, 0, -1))

---------------

def reverseseq(n):
    return [x for x in range(n, 0, -1)]

---------------

reverse_seq = lambda n: list(range(n, 0, -1))

---------------
"""
