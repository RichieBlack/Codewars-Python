"""
@File    : Define a card suit.py 
@Author  : Richie Black
@Time    : 28.10.2022 12:44

I have been learning Python since August 2022.
"""


def define_suit(card):
    if card[-1] == 'C':
        return 'clubs'
    elif card[-1] == 'D':
        return 'diamonds'
    elif card[-1] == 'H':
        return 'hearts'
    elif card[-1] == 'S':
        return 'spades'


"""Best practices
-----------------

def define_suit(card):
    d = {'C': 'clubs', 'S':'spades', 'D':'diamonds','H':'hearts'}
    return d[card[-1]]

-----------------

def define_suit(card):
    return {'C':'clubs', 'S':'spades', 'D':'diamonds', 'H':'hearts'}[card[-1]]

-----------------

define_suit = lambda card: {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}[card[-1]]

-------------
"""

# https://www.codewars.com/kata/reviews/5a3bb928f4f64c826c0012f0/groups/63358166ee5fc70001adf992
