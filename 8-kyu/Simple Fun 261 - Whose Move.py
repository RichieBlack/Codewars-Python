"""
@File    : Simple Fun 261 - Whose Move.py 
@Author  : Richie Black
@Time    : 06.11.2022 2:59

I have been learning Python since August 2022.
"""


def whoseMove(lastPlayer, win):
    if lastPlayer == "black" and win == False:
        return "white"

    elif lastPlayer == "white" and win == True:
        return "white"

    else:
        return "black"


"""Best practices
-----------------

def whoseMove(lastPlayer, win):
    return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'

-----------------

def whoseMove(lastPlayer, win):
    players = ['white', 'black']
    return lastPlayer if win else players[players.index(lastPlayer) - 1]

-----------------

def whoseMove(lastPlayer, win):
    return ["white", "black"][(lastPlayer == "black") == win]

-----------------
"""

# https://www.codewars.com/kata/reviews/5913499ac4e54e6e44000071/groups/6366eb2580a9b40001788e79
