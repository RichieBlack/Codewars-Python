# link: https://www.codewars.com/kata/reviews/55872716e678de23d40000bb/groups/59cf63fdc5c199e1b2000033

def digitize(n):
    return [int(s) for s in str(n)][::-1]

'''
Best practices
--------------

def digitize(n):
    return map(int, str(n)[::-1])

--------------

def digitize(n):
    return [int(x) for x in str(n)[::-1]]

--------------
'''