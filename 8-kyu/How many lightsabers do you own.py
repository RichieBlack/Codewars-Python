"""
@File    : How many lightsabers do you own.py 
@Author  : Richie Black
@Time    : 22.10.2022 21:11

I have been learning Python since August 2022.
"""


def how_many_light_sabers_do_you_own(name=0):
    if name == 'Zach':
        return 18
    else:
        return 0


"""Best practices
-----------------

def how_many_light_sabers_do_you_own(name=""):
    return 18 if name == "Zach" else 0

-----------------

def howManyLightsabersDoYouOwn(*name):
    return 18 if name == ('Zach',) else 0

-----------------

howManyLightsabersDoYouOwn = lambda n="": 18 * (n == "Zach")

-----------------
"""

# https://www.codewars.com/kata/reviews/54128ec1648162a633000020/groups/632ad0907107960001c7a1e3
