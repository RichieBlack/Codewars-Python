# https://www.codewars.com/kata/reviews/568304e7c0c0e6d62000005f/groups/5fe36c793d2da50001adf09c

def find_needle(haystack):
    index = 0
    for i in haystack:
        if i == "needle":
            return f'found the needle at position {index}'
        index += 1


# I have been studying Python for one month.

"""Best practices
-----------------

def find_needle(haystack):
    return 'found the needle at position %d' % haystack.index('needle')

-----------------

def find_needle(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))

-----------------

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'

-----------------
"""
