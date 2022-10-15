# link:

def multiply(a, b):
    return(a * b)

'''
Best practices
--------------

def multiply(a, b):
  return a * b

--------------

def multiply(a, b):
    if isinstance(a, (int, float, complex)):
        if isinstance(b, (int, float, complex)):
            return a * b

--------------

multiply = lambda x, y: x * y

--------------

multiply = __import__('operator').mul

--------------
'''