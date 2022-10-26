"""
@File    : USD - CNY.py 
@Author  : Richie Black
@Time    : 26.10.2022 23:17

I have been learning Python since August 2022.
"""


def usdcny(usd):
    return "{:.2f} Chinese Yuan".format(usd * 6.75)


"""Best practices
-----------------

def usdcny(usd):
    return f"{(usd * 6.75):.2f} Chinese Yuan"

-----------------

COURSE = 6.75  # CNY == 1 USD


def usdcny(usd):
    return f"{usd * COURSE:.2f} Chinese Yuan"

-----------------

usdcny = lambda u: f"{6.75 * u:.2f} Chinese Yuan"

-----------------
"""

# https://www.codewars.com/kata/reviews/613f3d1fcc9d3c0001482fee/groups/632e2d700c918200016deeaf
