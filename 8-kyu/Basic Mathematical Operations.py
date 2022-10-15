# link: https://www.codewars.com/kata/reviews/57b15e5c8a36ac1d4600005c/groups/61d784565775fa00015171f0

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


'''
Best practices
--------------

def basic_op(operator, value1, value2):
    if operator=='+':
        return value1 + value2
    if operator=='-':
        return value1 - value2
    if operator=='/':
        return value1 / value2
    if operator=='*':
        return value1 * value2

--------------

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

--------------

def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

--------------

basic_op = lambda op, v1, v2: eval("{}{}{}".format(v1, op, v2))

--------------

def basic_op(op, v1, v2):
    return v1 + v2 if op == "+" else v1 - v2 if op == "-" else  v1 * v2 if op == "*" else  v1 / v2

--------------
'''