"""
@File    : Student's Final Grade.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:11

I have been learning Python since August 2022.
"""


def final_grade(exam, projects):
    final_grade = 0

    if exam > 90 or projects > 10:
        final_grade = 100
    elif exam > 75 and projects >= 5:
        final_grade = 90
    elif exam > 50 and projects >= 2:
        final_grade = 75
    elif exam <= 50 or projects <= 2:
        final_grade = 0

    return final_grade


"""Best practices
-----------------

def final_grade(exam, projects):
    if exam > 90 or projects > 10: return 100
    if exam > 75 and projects >= 5: return 90
    if exam > 50 and projects >= 2: return 75
    return 0

-----------------

def final_grade(exam, projects):
    return 100 if exam > 90 or projects > 10 else 90 if exam > 75 and projects >= 5 else 75 if exam > 50 and projects >=2 else 0

-----------------

def final_grade(x, p):
    return ( (x>90 or p>10) and 100 or 
             x>75 and p>=5 and 90 or
             x>50 and p>=2 and 75 or 0)

-----------------
"""

# https://www.codewars.com/kata/reviews/5c3ccb692ce7350001bde463/groups/6328b7ef1ed846000190d4d6
