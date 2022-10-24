"""
@File    : Multiplication table for number.py 
@Author  : Richie Black
@Time    : 24.10.2022 22:35

I have been learning Python since August 2022.
"""


def multi_table(number):
    table = ''
    result = 1

    for i in range(1, 11):
        result = i * number
        table += str(i) + ' * ' + str(number) + ' = ' + str(result) + '\n'
    table = table[:-1]
    return table


"""Best practices
-----------------

def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))

-----------------

def multi_table(number):
    table = ["{0} * {1} = {2}".format(i, number, i * number) for i in range(1, 11)]
    return '\n'.join(table)

-----------------

def multi_table(n):
    return '\n'.join(f'{i} * {n} = {i*n}' for i in range(1, 11))

-----------------
"""

# https://www.codewars.com/kata/reviews/5a3131b016f1018d3c0015c8/groups/632af63be566c10001e06f26
