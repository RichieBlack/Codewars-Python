# link: https://www.codewars.com/kata/reviews/55a709464d8e6220280000c9/groups/61d62825ae575c0001525069

def greet(name):
    return "Hello, " + name + " how are you doing today?"


'''
Best practices
--------------

def greet(name):
    return f'Hello, {name} how are you doing today?'

--------------

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

--------------

def greet(name):
    return "Hello, " + name + " how are you doing today?"

--------------

greet = lambda name: f'Hello, {name} how are you doing today?'

--------------
'''