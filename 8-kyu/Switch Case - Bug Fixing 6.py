"""
@File    : Switch Case - Bug Fixing 6.py 
@Author  : Richie Black
@Time    : 30.10.2022 14:27

I have been learning Python since August 2022.
"""


def eval_object(v):
    match v['operation']:
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1


"""Best practices
-----------------

def eval_object(v):
    return {"+": v['a']+v['b'],
            "-": v['a']-v['b'],
            "/": v['a']/v['b'],
            "*": v['a']*v['b'],
            "%": v['a']%v['b'],
           "**": v['a']**v['b'], }.get(v['operation'])

-----------------

def eval_object(v):
    return eval("{a}{operation}{b}".format(**v))

-----------------

def eval_object(v):
    return eval(str(v['a']) + v['operation'] + str(v['b']))

-----------------
"""

# https://www.codewars.com/kata/reviews/55ce88529de501f508000073/groups/63447771f8854e0001893025
