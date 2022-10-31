"""
@File    : Calculate Price Excluding VAT.py 
@Author  : Richie Black
@Time    : 31.10.2022 19:19

I have been learning Python since August 2022.
"""


def excluding_vat_price(price):
    try:
        return round(price / 1.15, 2)
    except Exception:
        return -1


"""Best practices
-----------------

def excludingVatPrice(price):
    return round(price / 1.15, 2) if price else -1

-----------------

def excluding_vat_price(price):
    try:
        return round(price / 1.15, 2)
    except TypeError:
        return -1

-----------------

def excludingVatPrice(price, VAT=0.15):
    return round(price / (1 + VAT), 2) if price else -1

-----------------
"""

# https://www.codewars.com/kata/reviews/589417919f91118f7e000680/groups/635d5ea82d02960001bfb6f7
