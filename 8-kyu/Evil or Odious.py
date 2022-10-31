"""
@File    : Evil or Odious.py 
@Author  : Richie Black
@Time    : 31.10.2022 18:47

I have been learning Python since August 2022.
"""


def evil(n):
    return "It's Evil!" if not (bin(n).count('1')) % 2 else "It's Odious!"


"""Best practices
-----------------

def evil(n):
    return "It's Evil!" if  bin(n).count('1') % 2 == 0 else "It's Odious!"

-----------------

def evil(n):
    return "It's %s!" % ["Evil","Odious"][bin(n).count("1") % 2]

-----------------

def evil(n):
    return 'It\'s {}!'.format(('Evil', 'Odious')[bin(n).count('1') % 2])

-----------------
"""

# https://www.codewars.com/kata/reviews/56fcfadbc7e1fa2472000036/groups/634f2dc7b7fb4e0001c45298
