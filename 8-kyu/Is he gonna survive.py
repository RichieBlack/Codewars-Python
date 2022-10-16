# https://www.codewars.com/kata/reviews/5bbcd151b6dfbbaa3400248c/groups/5bbd0cec484fcd189c0010a4

def hero(bullets, dragons):
    return True if bullets >= dragons * 2 else False


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def hero(bullets, dragons):
    return bullets >= dragons * 2

---------------

def hero(bullets, dragons):
    '''
    Ascertains if hero can survive
    Parameters:
        bullets: (int) - number of bullets hero has
        dragons: (int) - number of dragons
    Returns:
        True (Survive) or False (Hero gets killed)
    '''
    if bullets >= 2*dragons:
        return True
    elif bullets < 2*dragons:
        return False

---------------

hero = lambda b, d: 2 * d <= b

---------------
"""
