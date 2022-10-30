"""
@File    : NBA full 48 minutes average.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:55

I have been learning Python since August 2022.
"""


def nba_extrap(ppg, mpg):
    return round(((48 / mpg) * ppg), 1) if mpg != 0 else 0


"""Best practices
-----------------

def nba_extrap(ppg, mpg):
    return round(48.0 / mpg * ppg, 1) if mpg > 0 else 0

-----------------

def nba_extrap(ppg, mpg):
    return round(ppg * 48.0 / mpg, 1) if mpg else 0

-----------------

def nba_extrap(ppg, mpg):
    try:
        return round(ppg / (mpg * 1.0) * 48, 1) 
    except ZeroDivisionError:
        return 0


-----------------

def nba_extrap(ppg, mpg):
    return round(48 * ppg / mpg, 1)
    
-----------------
"""

# https://www.codewars.com/kata/reviews/587c2d0cbb65b5e8040004ff/groups/6344c499a96acf0001485333
