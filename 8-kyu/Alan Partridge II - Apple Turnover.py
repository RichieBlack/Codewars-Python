"""
@File    : Alan Partridge II - Apple Turnover.py 
@Author  : Richie Black
@Time    : 25.10.2022 19:34

I have been learning Python since August 2022.
"""


def apple(x):
    return (
        'It\'s hotter than the sun!!'
        if int(x) ** 2 > 1000
        else
        'Help yourself to a honeycomb Yorkie for the glovebox.'
    )


"""Best practices
-----------------

def apple(x):
  return ("It's hotter than the sun!!" if int(x) ** 2 > 1000 
         else  "Help yourself to a honeycomb Yorkie for the glovebox."
         )

-----------------

def apple(x):
    if int(x) ** 2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."

-----------------

def apple(x):
    if int(x) > 31:
        return "It's hotter than the sun!!" 
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."   

-----------------

def apple(x):
    return ("Help yourself to a honeycomb Yorkie for the glovebox.","It's hotter than the sun!!")[int(x) ** 2 > 1000]

-----------------
"""

# https://www.codewars.com/kata/reviews/580b6361e642940044000031/groups/632dc17c5f07700001c97b35
