"""
@File    : Test_simple.py
@Author  : Richie Black
@Time    : 19.10.2022 10:30

I have been learning Python since August 2022.
"""

from datetime import datetime


def is_today(date):
    x = datetime.now().strftime('%x')
    y = date.strftime('%x')

    return x == y


"""Best practices
-----------------

from datetime import datetime


def is_today(date):
    return date.date() == datetime.today().date()

-----------------

from datetime import datetime

def is_today(date):
    return date.strftime('%d-%m-%Y') == datetime.today().strftime('%d-%m-%Y')

-----------------

import datetime

def is_today(date):
    today = datetime.datetime.today()

    if date.day == today.day:
        return True
    else:
        return False

-----------------
"""
# https://www.codewars.com/kata/reviews/6221604c4368e40001533bc4/groups/634f9ec0fbff4500011b5678
