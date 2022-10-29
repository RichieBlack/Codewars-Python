"""
@File    : Price of Mangoes.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:27

I have been learning Python since August 2022.
"""


def mango(quantity, price):
    return (quantity - quantity // 3) * price


"""Best practices
-----------------

def mango(quantity, price):
    return (quantity - quantity // 3) * price

-----------------

def mango(quantity, price):
    return (quantity - int(quantity / 3))  * price

-----------------

mango = lambda count, price: (count - count // 3) * price

-----------------
"""

# https://www.codewars.com/kata/reviews/57a7da0a8450794e6b00011a/groups/63409a9dff928300014881f5
