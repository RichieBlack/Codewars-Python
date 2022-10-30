"""
@File    : Online RPG - player to qualifying stage.py 
@Author  : Richie Black
@Time    : 30.10.2022 22:57

I have been learning Python since August 2022.
"""


def playerRankUp(pts):
    return (
        'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'
        if pts >= 100
        else False
    )


"""Best practices
-----------------

def playerRankUp(pts):
    msg = "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." 
    return msg if pts >= 100 else False

-----------------

def playerRankUp(pts):
    return ("Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." 
            if pts >= 100 else False
            )

-----------------

def playerRankUp(pts):
    return [False, 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'][
    pts >= 100]

-----------------
"""

# https://www.codewars.com/kata/reviews/5593781b091cf8643e000099/groups/6345fc6f8c27ed00016fee77
