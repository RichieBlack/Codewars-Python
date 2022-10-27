"""
@File    : Triple Trouble.py 
@Author  : Richie Black
@Time    : 27.10.2022 13:58

I have been learning Python since August 2022.
"""


def triple_trouble(one, two, three):
    a, b, c = list(one), list(two), list(three)
    res = ''

    for i in range(len(one)):
        res = res + ''.join(a[i] + b[i] + c[i])

    return res


"""Best practices
-----------------

def triple_trouble(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))

-----------------

def triple_trouble(one, two, three):
    return "".join(a + b + c for a, b , c in zip(one,two,three))

-----------------

def triple_trouble(*args):
        return "".join("".join(a) for a in zip(*args))

-----------------

def triple_trouble(*args):
    return ''.join(sum(zip(*args), ()))
    
-----------------
"""

# https://www.codewars.com/kata/reviews/5705b031d4263bde6c000099/groups/6331e47bba5f4d0001ec4ce3
