"""
@File    : Is every value in the array an array.py 
@Author  : Richie Black
@Time    : 07.11.2022 22:23

I have been learning Python since August 2022.
"""


def arr_check(arr):
    check_list = []

    for item in arr:
        if isinstance(item, list):
            check_list.append(True)

        else:
            check_list.append(False)

    if False in check_list:
        return False
    else:
        return True


"""Best practices
-----------------

def arr_check(arr):
    return all(isinstance(el, list) for el in arr)

-----------------

def arr_check(arr):
    return all(type(i) == list for i in arr)

-----------------
"""

# https://www.codewars.com/kata/reviews/5831dd6615c02223780000d3/groups/63694e46c820700001eea439
