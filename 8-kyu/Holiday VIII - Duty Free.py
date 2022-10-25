"""
@File    : Holiday VIII - Duty Free.py 
@Author  : Richie Black
@Time    : 25.10.2022 18:54

I have been learning Python since August 2022.
"""


def duty_free(price, discount, holiday_cost):
    return int(holiday_cost / (price * (discount / 100)))


"""Best practices
-----------------

def duty_free(price, discount, holiday_cost):
    saving = price * discount / 100.0
    return int(holiday_cost / saving)

-----------------

def duty_free(price, discount, holiday_cost):
  return holiday_cost // (price * (discount / 100))

-----------------

def duty_free(price, discount, holiday_cost):
  return holiday_cost * 100 // price // discount

-----------------
"""

# https://www.codewars.com/kata/reviews/585267fb18ea6d92bd000ebc/groups/632c71547159d60001866771
