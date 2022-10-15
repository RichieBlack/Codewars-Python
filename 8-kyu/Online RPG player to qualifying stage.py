# link: https://www.codewars.com/kata/55849d76acd73f6cc4000087/python

def playerRankUp(pts):
    return (
        'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'
        if pts >= 100
        else False
    )

# I have been studying Python for two months.

'''
Best practices
--------------

def playerRankUp(pts):
    msg = "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." 
    return msg if pts >= 100 else False

--------------

def playerRankUp(pts):
    return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up." if pts >= 100 else False

--------------

playerRankUp = lambda p: False if p < 100 else "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."

--------------
'''