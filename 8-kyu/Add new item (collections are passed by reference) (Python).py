"""
@File    : Add new item (collections are passed by reference) (Python).py 
@Author  : Richie Black
@Time    : 06.12.2022 19:37

I have been learning Python since August 2022.
"""


def add_extra(list_of_numbers):
    thirteen = [13]
    return list_of_numbers + thirteen


"""Best practices
-----------------

def AddExtra(listOfNumbers):
    return listOfNumbers + [13]

-----------------
"""

# https://www.codewars.com/kata/reviews/56e2951ec7a794066f000002/groups/638dcc5bd805df00019d9bb0