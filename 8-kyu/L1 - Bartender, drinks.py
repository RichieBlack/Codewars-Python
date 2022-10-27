"""
@File    : L1 - Bartender, drinks.py 
@Author  : Richie Black
@Time    : 27.10.2022 7:13

I have been learning Python since August 2022.
"""


def get_drink_by_profession(param):
    a = {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }
    if param.title() in a:
        return a.get(param.title())
    else:
        return 'Beer'


"""Best practices
-----------------

d = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal"
}


def get_drink_by_profession(s):
    return d.get(s.lower(), "Beer")

-----------------

def get_drink_by_profession(param):
    return {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }.get(param.title(), "Beer")

-----------------

def get_drink_by_profession(param):
    d = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", "Programmer":"Hipster Craft Beer", 
        "Bike Gang Member":"Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"
        }
    if param.title() in d:
        return d[param.title()]
    else:
        return "Beer"

-----------------
"""

# https://www.codewars.com/kata/reviews/5e72114a76b67f0001b0388a/groups/6330624795410400014c8f60
