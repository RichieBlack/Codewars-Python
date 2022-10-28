"""
@File    : Return the day.py 
@Author  : Richie Black
@Time    : 28.10.2022 20:07

I have been learning Python since August 2022.
"""


def whatday(num):
    return {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }[num] if 0 < num < 8 else 'Wrong, please enter a number between 1 and 7'


"""Best practices
-----------------

WEEKDAY = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday' }
ERROR = 'Wrong, please enter a number between 1 and 7'


def whatday(n):
    return WEEKDAY.get(n, ERROR)

-----------------

def whatday(num):
    days = ('Sun', 'Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur')
    return days[num - 1] + 'day' if 0 < num < 8 else 'Wrong, please enter a number between 1 and 7' 

-----------------

whatday = lambda n: 'Wrong, please enter a number between 1 and 7' * (
                    n > 7 or n < 1) or __import__('calendar').day_name[n - 2]

-----------------
"""

# https://www.codewars.com/kata/reviews/5c4d3ffb3c03c900014bc0af/groups/6335f726bf272700015adacc
