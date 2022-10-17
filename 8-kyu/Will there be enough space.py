# https://www.codewars.com/kata/reviews/5875b204d520904a04000005/groups/632103ffc16e640001dd9480

def enough(cap, on, wait):
    n = (cap - on)
    if wait < n:
        return 0
    else:
        return wait - n


# I have been studying Python for one month.

"""Best practices
-----------------

def enough(cap, on, wait):
    return max(0, wait - (cap - on))

-----------------

def enough(cap, on, wait):
    return wait + on - cap if wait + on > cap else 0

-----------------

enough = lambda c, o, w: max(0, w - (c - o))

-----------------
"""
