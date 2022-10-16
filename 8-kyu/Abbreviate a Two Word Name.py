# https://www.codewars.com/kata/reviews/5adf24ac82c8a1c88100176e/groups/631cc91c1688410001ec1ee9

def abbrev_name(name):
    init = name.split()
    N = init[0]
    M = init[1]
    return N[0:1:].upper() + '.' + M[0:1:].upper()


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

---------------

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]

---------------

def abbrevName(name):
    return name.split(' ')[0][0].upper()+'.'+name.split(' ')[1][0].upper()

---------------

def abbrevName(name):
    return '.'.join(filter(str.isupper,name.title()))

---------------
"""