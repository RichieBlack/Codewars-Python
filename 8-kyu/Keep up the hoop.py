"""
@File    : Keep up the hoop.py 
@Author  : Richie Black
@Time    : 21.10.2022 20:53

I have been learning Python since August 2022.
"""


def hoop_count(n):
    return 'Great, now move on to tricks' if n >= 10 else 'Keep at it until you get it'


"""Best practices
-----------------

def hoopCount(n):
    return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"

-----------------

def hoopCount(n):
    if n < 0:
        return "Really now...?"
    
    elif n < 10:
        return "Keep at it until you get it"
    
    else:
        return "Great, now move on to tricks"

-----------------

def hoopCount(n):
    return ("Great, now move on to tricks", "Keep at it until you get it")[n < 10]

-----------------
"""

# https://www.codewars.com/kata/reviews/55d197698a9fa10be300005c/groups/63288482cc4a1200016c42b0
