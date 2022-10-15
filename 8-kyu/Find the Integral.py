def integrate(coefficient, exponent):
    return f'{int(coefficient / (exponent + 1))}x^{exponent + 1}'

# I have been studying Python for two months.

'''
Best practices
--------------

def integrate(coef, exp):
    exp = exp + 1
    coef = coef / exp if coef % exp else coef // exp
    return f"{coef}x^{exp}"

--------------

def integrate(c, e):
    return f"{c / (e+1)}x^{e+1}".replace(".0x", "x")

--------------
'''