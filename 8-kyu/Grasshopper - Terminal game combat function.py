"""
@File    : Grasshopper - Terminal game combat function.py 
@Author  : Richie Black
@Time    : 26.10.2022 20:43

I have been learning Python since August 2022.
"""


def combat(health, damage):
    return health - damage if damage < health else 0


"""Best practices
-----------------

def combat(health, damage):
    return max(0, health - damage)

-----------------

def combat(health, damage):
    return health - damage if health > damage else 0

-----------------

combat = lambda h, d: (h > d) * (h - d)

-----------------
"""

# https://www.codewars.com/kata/reviews/586cd91ce8e8d451ec000b14/groups/632de19cee1c3f00017f4fae
