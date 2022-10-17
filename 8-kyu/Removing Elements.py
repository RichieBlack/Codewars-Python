# https://www.codewars.com/kata/reviews/5769b390cdd98d7959000ab9/groups/576c37651f82f419970001f1

def remove_every_other(my_list):
    return my_list[::2]


# I have been studying Python for one month.

"""Best practices
-----------------

def remove_every_other(my_list):
    return my_list[::2]

-----------------

def remove_every_other(my_list):
    r = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            r.append(my_list[i])
    return r

-----------------

def remove_every_other(my_list):
    return [v for c, v in enumerate(my_list) if not c % 2]

-----------------
"""
