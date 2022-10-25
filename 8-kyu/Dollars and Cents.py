"""
@File    : Dollars and Cents.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:30

I have been learning Python since August 2022.
"""


def format_money(amount):
    return "${:.2f}".format(round(amount, 2))


"""Best practices
-----------------

def format_money(amount):
    return '${:.2f}'.format(amount)

-----------------

def format_money(amount):
    return '$%0.2f' % amount

-----------------

def format_money(amount):
    # your formatting code here
    return f'${amount:.2f}'

-----------------

format_money = lambda x: '${:.2f}'.format(x)

-----------------
"""

# https://www.codewars.com/kata/reviews/55903973aa8069036c0000ab/groups/632d71fbee1c3f00017f3364
