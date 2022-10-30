"""
@File    : Find the Integral.py
@Author  : Richie Black
@Time    : 25.10.2022 12:27

I have been learning Python since August 2022.
"""


def integrate(coefficient, exponent):
    return f'{int(coefficient / (exponent + 1))}x^{exponent + 1}'


'''
Best practices
--------------

def integrate(coef, exp):
    exp = exp + 1
    coef = coef / exp if coef % exp else coef // exp
    return f"{coef}x^{exp}"

--------------

def integrate(c, e):
    return f"{c / (e+1)}x^{e+1}".replace(".0x", "x")

--------------
'''

# https://www.codewars.com/kata/reviews/5c3e18c0478204000135e5c1/groups/63474dda7b911e0001bc8fdb
