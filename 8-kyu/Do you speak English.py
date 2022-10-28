"""
@File    : Do you speak English.py 
@Author  : Richie Black
@Time    : 28.10.2022 19:51

I have been learning Python since August 2022.
"""


def sp_eng(sentence):
    s = sentence.lower()
    return s.find('english') > -1


"""Best practices
-----------------

def sp_eng(sentence): 
    return 'english' in sentence.lower()

-----------------

sp_eng = lambda _: 'english' in _.lower()

-----------------

def sp_eng(sentence): 
    return True if 'english' in sentence.lower() else False

-------------
"""

# https://www.codewars.com/kata/reviews/60760137bd7f6700015e6221/groups/6335a95eee5fc70001ae03ab
