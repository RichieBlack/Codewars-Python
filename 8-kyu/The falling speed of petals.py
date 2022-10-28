"""
@File    : The falling speed of petals.py 
@Author  : Richie Black
@Time    : 28.10.2022 12:40

I have been learning Python since August 2022.
"""


def sakura_fall(v):
    #   the height of the cherry is 5 * 80 = 400 cm
    return 400 / v if v > 0 else 0


"""Best practices
-----------------

def sakura_fall(v):
    return 400 / v if v > 0 else 0

-----------------

def sakura_fall(v):
    return v > 0 and 400 / v

-----------------

sakura_fall = lambda s: 400 / s if s > 0 else 0

-------------

# https://www.codewars.com/kata/reviews/5a0c2b24694efaaf9700004e/groups/6334ac50b0221700016b6953
