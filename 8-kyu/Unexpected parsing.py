"""
@File    : Unexpected parsing.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:42

I have been learning Python since August 2022.
"""


def get_status(is_busy):
    return {"status": "busy"} if is_busy else {"status": "available"}


"""Best practices
-----------------

def get_status(is_busy):
    status = "busy" if is_busy else "available"
    return {"status": status}

-----------------

def get_status(is_busy): return {'status': ("busy" if is_busy else "available")}

-----------------

def get_status(is_busy):
    return {"status": "busy"} if is_busy else {"status": "available"}

-----------------
"""

# https://www.codewars.com/kata/reviews/564c83c2cd44043d9b000017/groups/634ec657cc8e290001edcc6f
