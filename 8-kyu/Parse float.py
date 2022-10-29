"""
@File    : Parse float.py 
@Author  : Richie Black
@Time    : 29.10.2022 11:37

I have been learning Python since August 2022.
"""


def parse_float(string):
    try:
        return float(string)
    except Exception:
        return None


"""Best practices
-----------------

def parse_float(string):
    try:
        return float(string)
    except:
        return None

-----------------

def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None

-----------------

def parse_float(s):
    if type(s) == str and __import__('re').match(r'[\d\.]+', s): return float(s)

-----------------
"""

# https://www.codewars.com/kata/reviews/57a98e63eb94c3a1ea000042/groups/6340a2b02575f00001cead4a
