# link: https://www.codewars.com/kata/reviews/55fad131365891dd35000159/groups/61f3c57f398ead00015ab586

def cockroach_speed(s):
    return int(s * 27.7778)

# I have been studying Python for one month.

'''
Best practices
--------------

def cockroach_speed(s):
    return s // 0.036

--------------

def cockroach_speed(s):
    cm_per_km = 100000
    sec_per_hour = 3600
    return int(s * cm_per_km / sec_per_hour)

--------------

cockroach_speed = lambda s: int(27.7778 * s)

--------------
'''
