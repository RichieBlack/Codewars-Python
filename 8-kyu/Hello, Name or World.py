"""
@File    : Hello, Name or World.py 
@Author  : Richie Black
@Time    : 25.10.2022 12:53

I have been learning Python since August 2022.
"""


def hello(name=""):
    if name:
        return f'Hello, {name.capitalize()}!'
    else:
        return 'Hello, World!'


"""Best practices
-----------------

def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

-----------------

def hello(name=""):
    return f"Hello, {name.capitalize() if name else 'World'}!"

-----------------

def hello(name=None):    
    if not name:
        return "Hello, World!"
    return "Hello, %s!"%(name.capitalize())
    
-----------------

hello = lambda name="": "Hello, {}!".format("World" if not name else name.capitalize())

-----------------
"""

# https://www.codewars.com/kata/reviews/5be6afa3de03d77ca40000b4/groups/632b85f044f5b900019c9fcd
