"""
@File    : Thinkful - Logic Drills Traffic light.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:17

I have been learning Python since August 2022.
"""


def update_light(current):
    if current == 'green':
        return 'yellow'
    elif current == 'yellow':
        return 'red'
    else:
        return 'green'


"""Best practices
-----------------

def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

-----------------

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."

-----------------

def update_light(current):
    color = ['green', 'yellow', 'red']
    return color[(color.index(current)+1)%len(color)]

-----------------

update_light = {"green":"yellow", "yellow":"red", "red":"green"}.get

-----------------
"""

# https://www.codewars.com/kata/reviews/58649887a1659ed6cb000074/groups/6325fcaa67e50c0001f77c75
