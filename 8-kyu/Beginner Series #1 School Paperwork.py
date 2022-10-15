# link: https://www.codewars.com/kata/reviews/55fa41d875e1368e3c000044/groups/6318d6362a73c200013ea48e

def paperwork(n, m):
    return 0 if n < 0 or m < 0 else n * m


'''
Best practices
--------------

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

--------------

def paperwork(n, m):
    return max(n, 0) * max(m, 0)

--------------

paperwork = lambda a, b: a * b if min(a, b) > 0 else 0

--------------
'''