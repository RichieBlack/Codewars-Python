"""
@File    : Crash Override.py 
@Author  : Richie Black
@Time    : 05.11.2022 0:58

I have been learning Python since August 2022.
"""

FIRST_NAME = {'B': 'Beta', 'D': 'Data', 'F': 'Function', 'H': 'Half-life', 'M': 'Malware', 'W': 'WiFi'}
SURNAME = {'K': 'Killer', 'M': 'Mike', 'P': 'Payload', 'T': 'T-Rex', 'W': 'Worm'}


def alias_gen(f_name, l_name):
    if f_name[0].isalpha() \
            and f_name[0].upper() in FIRST_NAME \
            and l_name[0].upper() in SURNAME:
        return f"{FIRST_NAME[f_name.upper()[0]]} {SURNAME[l_name.upper()[0]]}"

    else:
        return 'Your name must start with a letter from A - Z.'


"""Best practices
-----------------

def alias_gen(f_name, l_name):
    try:
        return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
    except:
        return 'Your name must start with a letter from A - Z.'

-----------------

def alias_gen(f_name, l_name):
    first = FIRST_NAME.get(f_name[0].upper())
    last = SURNAME.get(l_name[0].upper())
    return '{} {}'.format(first, last) if first and last else \
        'Your name must start with a letter from A - Z.'

-----------------

alias_gen = lambda f_name, l_name : "Your name must start with a letter from A - Z." \
                                    if ((f_name [0].upper () not in FIRST_NAME) \
                                        or (l_name [0].upper () not in SURNAME)) \
                                    else "{} {}".format (FIRST_NAME [f_name [0].upper ()], \
                                                            SURNAME [l_name [0].upper ()]);

-----------------
"""

# https://www.codewars.com/kata/reviews/578e09b016435603a2000072/groups/6367cfaa7c172000015a7045