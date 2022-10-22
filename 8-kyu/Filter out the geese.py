"""
@File    : Filter out the geese.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:45

I have been learning Python since August 2022.
"""


def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

    return [bird for bird in birds if not bird in geese]


"""Best practices
-----------------

geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}

def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

-----------------

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    return list(filter(lambda x: x not in geese, birds))

-----------------

goose_filter = lambda l:[e for e in l if e[:3] not in"AfrRomTouPilSte"]

-----------------
"""

# https://www.codewars.com/kata/reviews/59cf81c99efac1304e0001ea/groups/632a0455df13fb0001758e43
