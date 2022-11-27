"""
@File    : Is your period late.py 
@Author  : Richie Black
@Time    : 28.11.2022 1:18

I have been learning Python since August 2022.
"""

import datetime


def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length


"""Best practices
-----------------

def period_is_late(last, today, cycle_length):
    return (today - last).days > cycle_length

-----------------

def period_is_late(last,today,cycle_length):
    delta = today - last
    if delta.days > cycle_length:
        return True
    else:
        return False

-----------------

import datetime

def period_is_late(last,today,cycle_length):
    return today > (last + datetime.timedelta(days=cycle_length))

-----------------

period_is_late = lambda l, t, c: abs((t - l).days) > c

-----------------
"""

# https://www.codewars.com/kata/reviews/57908e6ae0e9549e860000af/groups/6383d31859836b0001c7c5ef
