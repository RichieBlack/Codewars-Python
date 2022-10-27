"""
@File    : How old will I be in 2099.py 
@Author  : Richie Black
@Time    : 27.10.2022 7:05

I have been learning Python since August 2022.
"""


def calculate_age(year_of_birth, current_year):
    how_old = current_year - year_of_birth
    a = f"You are {how_old} years old."
    b = "You were born this very year!"
    c = "You will be born in 1 year."
    d = "You are 1 year old."
    e = f"You will be born in {abs(how_old)} years."

    if how_old > 1:
        return a
    elif how_old == 0:
        return b
    elif how_old == -1:
        return c
    elif how_old == 1:
        return d
    else:
        return e


"""Best practices
-----------------

def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
        
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
        
    return 'You were born this very year!'

-----------------

def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    
    if age == 0:
       return "You were born this very year!"
       
    elif age > 0:
       return "You are {} year{} old.".format(age, 's' if age > 1 else '')
       
    else:
       return "You will be born in {} year{}.".format(abs(age), 's' if abs(age) > 1 else '')

-----------------

def calculate_age(birth, curr):
    diff = abs(curr - birth)
    age = "%d year%s" % (diff, "s" * bool(diff-1))
    
    return ("You were born this very year!" if not diff else "You are %s old." % age if curr > birth 
            else "You will be born in %s." % age
            )

-----------------
"""

# https://www.codewars.com/kata/reviews/5762f33f9102afaeeb00075f/groups/632f729456e8d300012fc021
