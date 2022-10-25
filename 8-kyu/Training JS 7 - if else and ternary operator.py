"""
@File    : Training JS 7 - if else and ternary operator.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:18

I have been learning Python since August 2022.
"""


def sale_hotdogs(n):
    #   ternary operator: <expression on true> if <predicate> else <expression on false>
    # --------------------
    return 100 * n if n < 5 else 95 * n if n >= 5 and n < 10 else 90 * n


#
#   more readable code:
# --------------------
def sale_hotdogs_alt(n):
    return (
        100 * n
        if n < 5
        else
        95 * n
        if n >= 5 and n < 10
        else
        90 * n
    )


#   simple code:
# ---------------------
def sale_hotdogs_alt2(n):
    if n < 5:
        price = 100
    elif n >= 5 and n < 10:
        price = 95
    else:
        price = 90
    return price * n


"""Best practices
-----------------

def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)

-----------------

def sale_hotdogs(n):
    return n * [90, 95, 100][(n < 10) + (n < 5)]

-----------------

def sale_hotdogs(n):
    rate = 100 if n < 5 else 95 if n < 10 else 90
    return n * rate

-----------------
"""

# https://www.codewars.com/kata/reviews/5723614c82e209fad5000157/groups/632ccf4adcc8310001273ede
