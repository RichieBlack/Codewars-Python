"""
@File    : Leonardo Dicaprio and Oscars.py 
@Author  : Richie Black
@Time    : 29.10.2022 0:56

I have been learning Python since August 2022.
"""


def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar == 87 or oscar < 86:
        return "When will you give Leo an Oscar?"
    else:
        return "Leo got one already!"


"""Best practices
-----------------

def leo(oscar):
    if oscar == 88:
            return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
            return "Not even for Wolf of wallstreet?!"
    elif oscar < 88:
            return "When will you give Leo an Oscar?"
    elif oscar > 88:
            return "Leo got one already!"

-----------------

def leo(oscar):
    if oscar <= 88:
        return {86: 'Not even for Wolf of wallstreet?!',
                88: 'Leo finally won the oscar! Leo is happy'}.get(
            oscar, 'When will you give Leo an Oscar?')
    return 'Leo got one already!'

-----------------

def leo(oscar):
    return  ("Leo got one already!",
             "When will you give Leo an Oscar?",
             "Not even for Wolf of wallstreet?!",
             "Leo finally won the oscar! Leo is happy")[(oscar == 86) + (oscar < 88) + 3 * (oscar == 88)]

-----------------
"""

# https://www.codewars.com/kata/reviews/56d4958c3f4faf407c00002d/groups/633d1d16a69a64000163c690
