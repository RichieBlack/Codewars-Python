# https://www.codewars.com/kata/reviews/579a66190ea0239c6a000056/groups/63237f9d362de000011c2160

def check_alive(health):
    return False if health <= 0 else True


# I have been studying Python for one month.

"""Best practices
-----------------

def check_alive(health: int) -> bool:
    return health > 0

-----------------

def check_alive(health):
    if health <= 0:
        return False
    else:
        return True

-----------------

def check_alive(health):
    return health > 0

-----------------
"""
