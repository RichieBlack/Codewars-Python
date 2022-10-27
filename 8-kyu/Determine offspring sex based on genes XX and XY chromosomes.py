"""
@File    : Determine offspring sex based on genes XX and XY chromosomes.py 
@Author  : Richie Black
@Time    : 27.10.2022 7:21

I have been learning Python since August 2022.
"""


def chromosome_check(sperm):
    if sperm == 'XYX':
        return 'Congratulations! You\'re going to have a Pink Srarkling Unicorn.'
    if sperm == 'YXY':
        return 'Congratulations! You\'re going to have a Non-binary Genderqueer.'
    elif sperm == 'XY':
        return 'Congratulations! You\'re going to have a son.'
    else:
        return 'Congratulations! You\'re going to have a daughter.'


"""Best practices
-----------------

def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')

-----------------

def chromosome_check(sperm):
    gender = {"XY" : "son", "XX" : "daughter"}
    
    return "Congratulations! You're going to have a {}.".format(gender[sperm])

-----------------

def chromosome_check(sperm):
    gender = 'son' if 'Y' in sperm else 'daughter'
    return f"Congratulations! You're going to have a {gender}."

-----------------

def chromosome_check(sperm):
    return "Congratulations! You're going to have a %s." % ('son', 'daughter')[sperm[1] == 'X']

-----------------
"""

# https://www.codewars.com/kata/reviews/579e76cf5460363df9000170/groups/63306659d979350001691d6c
