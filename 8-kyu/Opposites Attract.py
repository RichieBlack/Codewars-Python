# https://www.codewars.com/kata/reviews/555acb6d4f0c35acb5000084/groups/61ebf577dfe85a0001d79c0e

def lovefunc(flower1, flower2):
    if (flower1 % 2 == 0 and flower2 % 2 > 0) or (flower1 % 2 > 0 and flower2 % 2 == 0):
        return True
    else:
        return False


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2

---------------

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2

---------------

lovefunc = lambda a, b:(a + b) % 2

---------------
"""
