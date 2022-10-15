# link: https://www.codewars.com/kata/reviews/545878a4888e9859aa000210/groups/5ab098bb033e3f6fea000e68

def bool_to_word(boolean):
    return 'Yes' if boolean == True else 'No'


'''
Best practices
--------------

def bool_to_word(bool):
    return "Yes" if bool else "No"

--------------

bool_to_word = {True: 'Yes', False: 'No'}.get

--------------

bool_to_word = ['No', 'Yes'].__getitem__

--------------

bool_to_word = lambda b: b and "Yes" or "No"

--------------
'''