"""
@File    : Welcome to the City.py 
@Author  : Richie Black
@Time    : 26.10.2022 21:40

I have been learning Python since August 2022.
"""


def say_hello(name, city, state):
    name = ' '.join(name)
    return f'Hello, {name}! Welcome to {city}, {state}!'


"""Best practices
-----------------

def say_hello(name, city, state):
  return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)

-----------------

def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

-----------------

def say_hello(name, city, state):
    return 'Hello, %s! Welcome to %s, %s!' % (' '.join(name), city, state)

-----------------
"""

# https://www.codewars.com/kata/reviews/559375be091cf8fa99000050/groups/632e0a068f14580001903c58
