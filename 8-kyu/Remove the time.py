"""
@File    : Remove the time.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:18

I have been learning Python since August 2022.
"""


def shorten_to_date(long_date):
    return long_date.split(', ')[0]


"""Best practices
-----------------

def shorten_to_date(long_date):
    return long_date.split(',')[0]

-----------------

def shorten_to_date(long_date):
    return long_date[:long_date.index(',')]

-----------------

def shorten_to_date(long_date):
    return long_date[:long_date.rfind(',')]

-----------------
"""

# https://www.codewars.com/kata/reviews/56c5cdb06c6021354800008d/groups/633f9ff7ff9283000148489b
