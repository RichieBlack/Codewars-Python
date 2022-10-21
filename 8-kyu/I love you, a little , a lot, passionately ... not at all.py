"""
@File    : I love you, a little , a lot, passionately ... not at all.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:25

I have been learning Python since August 2022.
"""


def how_much_i_love_you(nb_petals):
    spells = {
        1: 'I love you',
        2: 'a little',
        3: 'a lot',
        4: 'passionately',
        5: 'madly',
        6: 'not at all'
    }

    if nb_petals % 6 == 1: return spells[1]
    if nb_petals % 6 == 2: return spells[2]
    if nb_petals % 6 == 3: return spells[3]
    if nb_petals % 6 == 4: return spells[4]
    if nb_petals % 6 == 5:
        return spells[5]
    else:
        return spells[6]


"""Best practices
-----------------

def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]

-----------------

def how_much_i_love_you(nb_petals):
    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
            5: 'madly', 0: 'not at all'}
    return words[nb_petals % 6]

-----------------

phrases = [
    'I love you',
    'a little',
    'a lot',
    'passionately',
    'madly',
    'not at all',
]

def how_much_i_love_you(n):
    return phrases[(n - 1) % len(phrases)]

-----------------

def how_much_i_love_you(nb_petals):
    return ["not at all", "I love you", "a little", "a lot", "passionately", "madly"][nb_petals % 6]
    
-----------------
"""

# https://www.codewars.com/kata/reviews/57f25c34c001bc9f3c000072/groups/6328d966a9ebca0001d35ed8