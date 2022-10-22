"""
@File    : Well of Ideas - Easy Version.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:43

I have been learning Python since August 2022.
"""


def well(x):
    count = 0

    if 'good' in x:
        count = x.count('good')

        if count < 3:
            return 'Publish!'
        elif count > 2:
            return 'I smell a series!'
    else:
        return 'Fail!'


"""Best practices
-----------------

def well(x):
    c = x.count('good')
    return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'

-----------------

def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"

-----------------

def well(x):
    if 'good' in x:
        return 'I smell a series!' if x.count('good') > 2 else 'Publish!'
    else:
        return 'Fail!'

-----------------

well = lambda x: ('Fail!','Publish!','I smell a series!')[('good' in x) + (x.count('good')>2)]

-----------------
"""

# https://www.codewars.com/kata/reviews/57f34bf9e7c28a0594000035/groups/6329d4a4bce8aa0001d64868
