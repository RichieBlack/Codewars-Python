# https://www.codewars.com/kata/reviews/59a1fa3ace67eff7b600053b/groups/6322025fb2d37c0001f3965a

def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b


# I have been studying Python for one month.

"""Best practices
-----------------

def solution(a, b):
    return a +b + a if len(a) < len(b) else b + a + b

-----------------

def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))

-----------------

def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short

-----------------
"""
