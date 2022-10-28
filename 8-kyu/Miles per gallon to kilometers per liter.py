"""
@File    : Miles per gallon to kilometers per liter.py 
@Author  : Richie Black
@Time    : 28.10.2022 19:55

I have been learning Python since August 2022.
"""


def converter(mpg):
    return (round((mpg * 1.609344) / 4.54609188, 2))


"""Best practices
-----------------

def converter(mpg):
    return round(mpg / 4.54609188 * 1.609344    , 2)

-----------------

converter = lambda x: round(x * 0.354006043538, 2)

-----------------

KM_PER_MILE = 1.609344
LITERS_PER_UK_GALLON = 4.54609188

def converter(mpg):
    return round(mpg * KM_PER_MILE / LITERS_PER_UK_GALLON, 2)

-------------
"""

# https://www.codewars.com/kata/reviews/5580400190c73741b700002b/groups/6335add7de9b6d0001b2b878
