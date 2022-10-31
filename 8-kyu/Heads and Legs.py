"""
@File    : Heads and Legs.py 
@Author  : Richie Black
@Time    : 31.10.2022 18:55

I have been learning Python since August 2022.
"""


def animals(heads, legs):
    """Suppose there are 72 "heads" and 200 "legs" .

    Let our cows has 2 "legs" and 2 "arms" a.k.a. forelimbs,
    then 72 "heads" has 144 "legs" and 56 "arms" (200-144=56).

    Finally we have 28 cows (56 : 2 = 28) and 44 chickens (72 - 28 = 44).
    """
    cows = legs - heads * 2

    if not cows % 2:
        cows = int(cows / 2)
    else:
        return "No solutions"

    chickens = heads - cows

    if heads == 0 and legs == 0:
        return (0, 0)
    elif (heads > 1000) or (legs > 1000) or (chickens < 0) or (cows < 0):
        return "No solutions"
    else:
        return (chickens, cows)


"""Best practices
-----------------

def animals(heads, legs):
    chickens, cows = 2 * heads - legs / 2, legs / 2 - heads
    if chickens < 0 or cows < 0 or not chickens == int(chickens) or not cows == int(cows):
        return "No solutions"
    return chickens, cows

-----------------

def animals(heads, legs):
    chickens = heads * 2 - legs / 2
    cows = heads - chickens
    if chickens < 0 or cows < 0 or chickens != int(chickens):
        return "No solutions"
    return chickens, cows

-----------------

def animals(heads, legs):
    solution = (2 * heads - legs / 2, legs / 2 - heads)
    return solution if legs % 2 == 0 and solution[0] >= 0 and solution[1] >= 0 else "No solutions"

-----------------
"""

# https://www.codewars.com/kata/reviews/574c94ba191025bcce00010d/groups/6350514db61a540001890f26
