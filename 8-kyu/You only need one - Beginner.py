# link: https://www.codewars.com/kata/reviews/57e922d73fad30057000004b/groups/5d7b318976056a0001170ae3

def check(seq, elem):
    for i in seq:
        if (i == elem):
            return True
    for i in seq:
        if (i != elem):
            return False


'''
Best practices
--------------

def check(seq, elem):
    return elem in seq

--------------

from operator import contains as check

--------------

def check(list, x):
    while True:
        if x in list:
            return True
        else:
            return False

--------------
'''