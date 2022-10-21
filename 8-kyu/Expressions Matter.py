"""
@File    : Expressions Matter.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:07

I have been learning Python since August 2022.
"""


def expression_matter(a, b, c):
    res = []

    res1 = (a + b) + c
    res2 = (a + b) * c
    res3 = (a * b) + c
    res4 = a + (b * c)
    res5 = a * (b + c)
    res6 = a * (b * c)

    res.append(res1)
    res.append(res2)
    res.append(res3)
    res.append(res4)
    res.append(res5)
    res.append(res6)

    return max(res)


"""Best practices
-----------------

def expression_matter(a, b, c):
    return max(a * b * c, a + b + c, (a + b) * c, a * (b + c))

-----------------

def expression_matter(a, b, c):
    cases = [a + b + c]
    cases.append(a * b * c)
    cases.append((a * b) + c)
    cases.append((a + b) * c)
    cases.append(a + (b * c))
    cases.append(a * (b + c))
    return max(cases)

-----------------

def expression_matter(a, b, c):
  return max(max(eval(f'{a}{op1}({b}{op2}{c})'), eval(f'({a}{op1}{b}){op2}{c}')) for op1 in '+*' for op2 in '+*')

-----------------
"""

# https://www.codewars.com/kata/reviews/5ae72ff2fdd6c33dbf001e71/groups/63288c58e952eb0001c03ba8
