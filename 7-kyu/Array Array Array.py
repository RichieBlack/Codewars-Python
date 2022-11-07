"""
@File    : Array Array Array.py 
@Author  : Richie Black
@Time    : 08.11.2022 0:40

I have been learning Python since August 2022.
"""


def explode(arr):
    if isinstance(arr[0], int) and isinstance(arr[1], int):
        return [arr for i in range(arr[0] + arr[1])]

    elif isinstance(arr[0], str) and isinstance(arr[1], int):
        return [arr for i in range(arr[1])]

    elif isinstance(arr[0], int) and isinstance(arr[1], str):
        return [arr for i in range(arr[0])]

    else:
        return 'Void!'


"""Best practices
-----------------

def explode(arr):  
    numbers = [n for n in arr if type(n) == int]
    return [arr] * sum(numbers) if numbers else "Void!"

-----------------

def explode(arr):
    if type(arr[0]) != int and type(arr[1]) != int:
        return "Void!"
    elif type(arr[0]) == int and type(arr[1]) != int:
        return [arr] * arr[0]
    elif type(arr[0]) != int and type(arr[1]) == int:
        return [arr] * arr[1]
    else:
        return [arr] * sum(arr)

-----------------

def explode(arr):
    [a, b] = arr
    if isinstance(a, int) and isinstance(b, int):
        time = a + b
    elif isinstance(a, str) and isinstance(b, int):
        time = b
    elif isinstance(a, int) and isinstance(b, str):
        time = a
    else:
        return 'Void!'
    return [arr] * time

-----------------
"""

# https://www.codewars.com/kata/reviews/5be1aef5587efa9ad20026cd/groups/63696de93947c400013855cd
