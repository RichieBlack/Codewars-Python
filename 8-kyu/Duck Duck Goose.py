"""
@File    : Duck Duck Goose.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:58

I have been learning Python since August 2022.
"""


def duck_duck_goose(players, goose):
    while len(players) < goose:
        goose = goose - len(players)
    return players[goose - 1].name


"""Best practices
-----------------

def duck_duck_goose(players, goose):
    return players[(goose % len(players)) - 1].name

-----------------

def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name

-----------------

def duck_duck_goose(players, goose):
  idx = (goose-1) % len(players)
  return players[idx].name

-----------------

duck_duck_goose = lambda players, goose: players[goose % len(players) - 1].name

-----------------
"""

# https://www.codewars.com/kata/reviews/5830c2a5e77f7d40bd000011/groups/634594e72ede9b0001c9f928
