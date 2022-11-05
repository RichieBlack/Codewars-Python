"""
@File    : Days in the year.py 
@Author  : Richie Black
@Time    : 06.11.2022 3:04

I have been learning Python since August 2022.
"""


def year_days(year):
    return (
        f"{year} has 365 days"
        if year % 4
           or not (year % 100) and (year % 400)
        else f"{year} has 366 days"
    )


"""Best practices
-----------------

def year_days(year):
    days = 365
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days += 1
    return "%d has %d days" % (year, days)

-----------------

from calendar import isleap


def year_days(year):
  return "{} has {} days".format(year, isleap(year) + 365)

-----------------

def year_days(year):
    return '{} has {} days'.format(year, 366 if year % 400 == 0 or (year % 4 == 0 and year % 100) else 365)

-----------------
"""

# https://www.codewars.com/kata/reviews/56d72513dd332dbe24000061/groups/6366f18abfa67f000139f8df
