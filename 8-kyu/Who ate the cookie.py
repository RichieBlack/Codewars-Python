"""
@File    : Who ate the cookie.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:27

I have been learning Python since August 2022.
"""


def cookie(x):
    match x:
        case (str(x)):
            return r"Who ate the last cookie? It was Zach!"
        case (bool(x)):
            return r"Who ate the last cookie? It was the dog!"
        case (int(x)) | (float(x)):
            return r"Who ate the last cookie? It was Monica!"
        case _:
            return r"Who ate the last cookie? It was the dog!"


def cookie_alt(x):
    """You must create a program that says who ate the last cookie.
    If the input is a string then "Zach" ate the cookie.
    If the input is a float or an int then "Monica" ate the cookie.
    If the input is anything else "the dog" ate the cookie.
    The way to return the statement is: "Who ate the last cookie? It was (name)!"

    Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach!
    (The reason you return Zach is because the input is a string)

    Note: Make sure you return the correct message with correct spaces and punctuation.
    """

    if isinstance(x, str):
        name = "Zach"

    if isinstance(x, (float, int)) and not isinstance(x, bool):
        name = "Monica"

    if isinstance(x, bool):
        name = "the dog"

    return f"Who ate the last cookie? It was {name}!"


"""Best practices
-----------------

def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

-----------------

def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who

-----------------

def cookie(x):
    #Good Luck
    if type(x) == type('x'):
        name = "Zach"
    elif type(x) == type(42) or type(x) == type(3.14):
        name = "Monica"
    else:
        name = "the dog"
    return "Who ate the last cookie? It was %s!"%name

-----------------
"""

# https://www.codewars.com/kata/reviews/55a99704c1eba8e2a20000a5/groups/634dc656f43981000121f069
# https://www.codewars.com/kata/reviews/55a99704c1eba8e2a20000a5/groups/634dbf5be3e35c00010651ee
