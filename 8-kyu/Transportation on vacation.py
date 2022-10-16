# link: https://www.codewars.com/kata/reviews/568d4e9827c5162bd600005a/groups/56c45130f1fe450687000c1b

def rental_car_cost(d):
    if d >= 7:
        return d * 40 - 50
    if d >= 3 and d < 7:
        return d * 40 - 20
    else:
        return d * 40

# I have been studying Python for one month.

"""
Best practices
--------------

def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result

--------------

def rental_car_cost(d):
    return d * 40 - (d > 2) * 20 - (d > 6) * 30

--------------

rental_car_cost = lambda d: d * 40 - (50 if d > 6 else 20 if d > 2 else 0)

--------------
"""
