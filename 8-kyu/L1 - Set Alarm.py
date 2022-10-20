"""
@File    : L1 - Set Alarm.py 
@Author  : Richie Black
@Time    : 20.10.2022 3:55

I have been learning Python since August 2022.
"""


def set_alarm(employed, vacation):
    return employed > vacation


"""Best practices
-----------------

def set_alarm(employed, vacation):
    return employed and not vacation

-----------------

def set_alarm(employed, vacation):
    if employed:
        if vacation:
            return False
        return True
    return False

-----------------

set_alarm = lambda *a: a == (1, 0)

-----------------
"""

# https://www.codewars.com/kata/reviews/5c2bd001b699cb00017ab489/groups/5c33e1b28a91780001bee2f2
