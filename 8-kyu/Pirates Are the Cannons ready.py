"""
@File    : Pirates Are the Cannons ready.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:26

I have been learning Python since August 2022.
"""


def cannons_ready(gunners):
    if 'nay' in gunners.values():
        return 'Shiver me timbers!'
    else:
        return 'Fire!'


"""Best practices
-----------------

def cannons_ready(gunners):
  return 'Shiver me timbers!' if 'nay' in gunners.values() else 'Fire!'

-----------------

def cannons_ready(gunners):
    for i in gunners:
        if gunners[i] == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'

-----------------

def cannons_ready(g):
  return ['Fire!','Shiver me timbers!']['nay' in g.values()]

-----------------
"""

# https://www.codewars.com/kata/reviews/5758525c0cb4b349c400006a/groups/63446d2db099e5000168fffe
