"""
@File    : Drink about.py 
@Author  : Richie Black
@Time    : 22.10.2022 20:50

I have been learning Python since August 2022.
"""


def people_with_age_drink(age):
    beverage = ''

    if age < 14:
        beverage = 'toddy'
    elif age < 18:
        beverage = 'coke'
    elif age < 21:
        beverage = 'beer'
    else:
        beverage = 'whisky'
    return f'drink {beverage}'


"""Best practices
-----------------

def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'

-----------------

def people_with_age_drink(age):
    if age <= 13:
        beverage = 'toddy'
    elif age > 13 and age <= 17:
        beverage = 'coke'
    elif age > 17 and age <= 20:
        beverage = 'beer'
    elif age > 20:
        beverage = 'whisky'
    return 'drink ' + beverage

-----------------

def people_with_age_drink(age):
    return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')

-----------------

def people_with_age_drink(age):
    for a in [[21,'whisky'],[18,'beer'],[14,'coke'],[0,'toddy']]:
        if age >= a[0]:
            return "drink {0}".format(a[1])
            
-----------------
"""

# https://www.codewars.com/kata/reviews/5644286755d0e476e6000096/groups/632a2790f5f54000010c6e65
