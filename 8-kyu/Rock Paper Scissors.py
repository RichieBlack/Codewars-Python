# https://www.codewars.com/kata/reviews/5672c704ea952f1e16000098/groups/6324a5919495b00001be7504

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'

    result = 0
    if p1 == 'rock':
        if p2 == 'scissors':
            result = 1
        else:
            result = 2

    if p1 == 'paper':
        if p2 == 'rock':
            result = 1
        else:
            result = 2

    if p1 == 'scissors':
        if p2 == 'paper':
            result = 1
        else:
            result = 2

    return f'Player {result} won!'


# I have been studying Python for one month.

"""Best practices
-----------------

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

-----------------

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

-----------------

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'

-----------------
"""
