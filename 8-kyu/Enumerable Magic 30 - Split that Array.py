"""
@File    : Enumerable Magic 30 - Split that Array.py 
@Author  : Richie Black
@Time    : 06.12.2022 19:29

I have been learning Python since August 2022.
"""


def partition(arr, classifier_method):
    first_arr = list(filter(classifier_method, arr))
    second_arr = []

    for i in arr:
        if i not in first_arr:
            second_arr.append(i)

    return (first_arr, second_arr)


"""Best practices
-----------------

def partition(list, classifier_method):
    listTrue = []
    listFalse = []
    for l in list:
        if classifier_method(l):
            listTrue.append(l)
        else:
            listFalse.append(l)
    return listTrue, listFalse

-----------------

from itertools import filterfalse


def partition(lis, classifier_method):
    fir = list(filter(classifier_method, lis))
    sec = list(filterfalse(classifier_method, lis))
    return (fir, sec)

-----------------

def partition(list, m):
    return ([x for x in list if m(x)],[x for x in list if not m(x)])

-----------------

def partition(arr, classifier_method):
    list1, list2 = [], [];

    for i in arr:
        if classifier_method(i):
            list1.append(i);
        else:
            list2.append(i);
            
    return (list1, list2)

-----------------

def partition(list, classifier_method):
    # one-liner:
    #return ([item for item in list if classifier_method(item)],
    #        [item for item in list if not classifier_method(item)])
    # fastest I found:
    
    true_list, false_list = [], []
    for item in list:
        (true_list if classifier_method(item) else false_list).append(item)
    return true_list, false_list

-----------------
"""

# https://www.codewars.com/kata/reviews/5be5ded6c7125cb332001af9/groups/638f5f543b7f36000194cf9d