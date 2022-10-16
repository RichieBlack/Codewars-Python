# https://www.codewars.com/kata/reviews/556a410ed44ca75d15000023/groups/556b30125c3a22bb9d00010b

def make_negative( number ):
    return number if number < 0 else -number


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def make_negative( number ):
    return -abs(number)

---------------

def make_negative( number ):
    return -number if number > 0 else number

---------------

def make_negative( number ):
    return -number if number>0 else number

---------------
"""