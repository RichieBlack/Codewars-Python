# https://www.codewars.com/kata/reviews/5b8533b67404e02cd7001407/groups/5b85a92ec7ebe5ac09000145

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - son_years_old * 2)


# I have been studying Python for one month.

"""Best practices
-----------------

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)

-----------------

twice_as_old = lambda d, s: ((d - s * 2)**2)**0.5

-----------------
"""
