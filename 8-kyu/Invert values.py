# https://www.codewars.com/kata/reviews/5899dc0f4382c462820015c4/groups/597e204806bd883d0e00002d

def invert(lst):
    inv = []
    for i in lst:
        i = i * -1
        inv.append(i)
    return inv


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def invert(lst):
    return [-x for x in lst]

---------------

def invert(lst):
    return list(map(lambda x: -x, lst))

---------------

def invert(lst):
   return [i * -1 for i in lst]

---------------
"""
