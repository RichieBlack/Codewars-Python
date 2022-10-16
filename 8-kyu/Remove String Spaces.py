# https://www.codewars.com/kata/reviews/58a18086c4931133bc0015c1/groups/58a18ec7c49311fbf3002011

def no_space(x):
    return "".join(x.split())


# I have been studying Python for one month.

"""
---------------
Best practices
---------------

def no_space(x):
    return x.replace(' ' ,'')

---------------

def no_space(x):
    return "".join(x.split())

---------------

no_space = lambda s: ''.join(filter(lambda ch: not ch == ' ', s))

---------------
"""