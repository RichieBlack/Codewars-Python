"""
@File    : Filtering even numbers (Bug Fixes).py 
@Author  : Richie Black
@Time    : 03.12.2022 20:38

I have been learning Python since August 2022.
"""


def kata_13_december(lst):
    temp = lst.copy()

    for i in lst:
        if i % 2 == 0:
            temp.remove(i)

    return temp


def kata_13_december_alt(lst):
    index = 0

    while index < len(lst):

        if lst[index] % 2 == 0:
            lst.pop(index)
        else:
            index += 1

    return lst


"""Best practices
-----------------

def kata_13_december(lst):
    return [item for item in lst if item & 1]

-----------------

def kata_13_december(lst): 
    return [x for x in lst if x % 2]

-----------------

def kata_13_december(lst): 
    new = list()
    for i in range(len(lst)): 
        if lst[i] % 2 != 0: 
            new.append(lst[i])
    return new

-----------------
"""

# https://www.codewars.com/kata/reviews/6119fe0f0dbc01000108ff4a/groups/638c8f71f4dbd8000197d5c3
#
# and alternative solution:
# https://www.codewars.com/kata/reviews/6119fe0f0dbc01000108ff4a/groups/638cec04ed0cd600019c5103
#
#
# Python Slicing (delete dublicates)
#
# list1 = [2, 3, 7, 3, 6, 2, 8, 8]
#
# index = 1
# while index < len(list1):
#     if list1[index] in list1[ : index]:
#         list1.pop(index)
#     else:
#         index += 1
#
# print(list1)
