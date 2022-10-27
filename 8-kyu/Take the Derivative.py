"""
@File    : Take the Derivative.py 
@Author  : Richie Black
@Time    : 27.10.2022 7:25

I have been learning Python since August 2022.
"""


def derive(coefficient, exponent):
    return (str(coefficient * exponent) + 'x^' + str(exponent - 1))


"""Best practices
-----------------

def derive(coefficient, exponent): 
    return f'{coefficient * exponent}x^{exponent - 1}'

-----------------

def derive(coefficient, exponent): 
    return("{}x^{}".format(coefficient*exponent, exponent-1))

-----------------

derive = lambda c, e: str(c * e) + "x^" + str(e - 1)

-----------------
"""

# https://www.codewars.com/kata/reviews/5eb54a9ac8df350001c7882b/groups/633082eea01cc500014dfb05
