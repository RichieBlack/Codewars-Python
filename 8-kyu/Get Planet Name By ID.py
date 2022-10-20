"""
@File    : Get Planet Name By ID.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:22

I have been learning Python since August 2022.
"""


def get_planet_name(id):
    name = ""
    match id:
        case 1:
            name = "Mercury"
        case 2:
            name = "Venus"
        case 3:
            name = "Earth"
        case 4:
            name = "Mars"
        case 5:
            name = "Jupiter"
        case 6:
            name = "Saturn"
        case 7:
            name = "Uranus"
        case 8:
            name = "Neptune"
    return name


"""Best practices
-----------------

def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)

-----------------

def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus", 
        8: "Neptune",
    }
    return planets[id]

-----------------

def get_planet_name(id):
    return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]

-----------------
"""

# https://www.codewars.com/kata/reviews/55937763289bb340cb000086/groups/632628f18704f6000157bf7d
