"""
@File    : A wolf in sheep's clothing.py 
@Author  : Richie Black
@Time    : 24.10.2022 22:46

I have been learning Python since August 2022.
"""


def warn_the_sheep(queue):
    pos_wolf = queue.index('wolf')
    pos_sheep = abs((pos_wolf) - (len(queue) - 1))

    if pos_wolf + 1 == len(queue):
        return 'Pls go away and stop eating my sheep'
    else:
        return f'Oi! Sheep number {pos_sheep}! You are about to be eaten by a wolf!'


"""Best practices
-----------------

def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return (f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n 
            else 'Pls go away and stop eating my sheep'
            )

-----------------

def warn_the_sheep(queue):
    i = queue[::-1].index('wolf')
    if i == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'


-----------------

def warn_the_sheep(queue):
    queue.reverse()
    return ('Pls go away and stop eating my sheep' if queue[0] == 'wolf' 
            else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))
            )

-----------------
"""

# https://www.codewars.com/kata/reviews/5c8d5f983b8ec2000120d031/groups/632b5f096d1bfe0001826158
