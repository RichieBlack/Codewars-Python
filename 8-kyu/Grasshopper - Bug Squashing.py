"""
@File    : Grasshopper - Bug Squashing.py 
@Author  : Richie Black
@Time    : 05.11.2022 0:37

I have been learning Python since August 2022.
"""

health = 100
position = 0
coins = 0


def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()


"""Best practices
-----------------

from preloaded import *

health = 100
position = 0
coins = 0


def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()

-----------------

health, position, coins = 100, 0, 0
log = 'roll_dice move combat get_coins buy_health print_status'.split(' ')


def main(): pass

-----------------

health = 100
position = 0
coins = 0


def main():
  [phase() for phase in[roll_dice, move, combat, get_coins, buy_health, print_status]]

-----------------
"""

# https://www.codewars.com/kata/reviews/563245c417f67074b700015f/groups/636578d772175e000194c0ed