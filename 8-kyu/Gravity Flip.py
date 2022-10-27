"""
@File    : Gravity Flip.py 
@Author  : Richie Black
@Time    : 27.10.2022 14:15

I have been learning Python since August 2022.
"""


def flip(d, a):
    if d == 'R': return sorted(a)
    if d == 'L': return sorted(a, reverse=True)


"""Best practices
-----------------

def flip(d,a):
    return sorted(a, reverse=d == 'L')

-----------------

def flip(d, a):
    if d == 'L':
        return sorted(a, reverse=True)
    else:
        return sorted(a)

-----------------

def flip(d, a):
    if d == 'R':
        a.sort()
        return a
    else:
        a.sort()
        a = a[::-1]
        return a

-----------------

def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a, reverse=True)
    
-----------------    
    
def flip(side, lst):
    return sorted(lst, reverse=(side == "L"))
    
-----------------  
"""

# https://www.codewars.com/kata/reviews/5f70c888e10f9e0001c89675/groups/63335bac68b0080001b9b343
