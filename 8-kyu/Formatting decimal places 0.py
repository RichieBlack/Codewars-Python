"""
@File    : Formatting decimal places 0.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:31

I have been learning Python since August 2022.
"""


def two_decimal_places(n):
    return round(n, 2)


"""Best practices
-----------------

def two_decimal_places(n):
    return round(n, 2)

-----------------

def two_decimal_places(n):
   return round(n * 100) / 100

-----------------

from decimal import Decimal, ROUND_HALF_UP


def two_decimal_places(n):
  dn = Decimal(str(n)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
  return float(dn)

-----------------

def two_decimal_places(n):
    return float("{0:.2f}".format(n))

-----------------
"""

# https://www.codewars.com/kata/reviews/564220d56003fa369c000036/groups/63342f57aecb6c0001fd747e
