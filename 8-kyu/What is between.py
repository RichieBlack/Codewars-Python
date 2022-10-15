# link: https://www.codewars.com/kata/reviews/573e427c18c24d7b2600002c/groups/573f386468e01f65d80001c5

def between(a, b):
    return list(range(a, b + 1))


'''
Best practices
--------------

def between(a,b):
    return list(range(a, b + 1))

--------------

def between(a,b):
    return [result for result in range(a, b + 1)]

--------------

def between(a,b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr

--------------

between=lambda a, b: list(range(a, b + 1))

--------------

between = lambda a, b: [n for n in range(a, b + 1)]

--------------
'''
