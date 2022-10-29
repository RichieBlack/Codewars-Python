"""
@File    : Fix your code before the garden dies.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:41

I have been learning Python since August 2022.
"""


def rain_amount(rain_amount):
    if (rain_amount < 40):
        return f"You need to give your plant {40 - rain_amount}mm of water"
    else:
        return "Your plant has had more than enough water for today!"


"""Best practices
-----------------

def rain_amount(mm):
    if mm < 40:
             return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
             return "Your plant has had more than enough water for today!"


-----------------

def rain_amount(mm):
    if mm < 40:
        return 'You need to give your plant {}mm of water'.format(40 - mm)
    return 'Your plant has had more than enough water for today!'

-----------------

rain_amount = lambda m: \
["Your plant has had more than enough water for today!", "You need to give your plant {}mm of water"][m < 40].format(
    40 - m)

-----------------
"""

# https://www.codewars.com/kata/reviews/5716bac801b0bfa81c000049/groups/634201e018860800019ccb7c
