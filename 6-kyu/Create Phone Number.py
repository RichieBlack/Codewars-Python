"""
@File    : Create Phone Number.py 
@Author  : Richie Black
@Time    : 23.10.2022 22:44

I have been learning Python since August 2022.
"""


def create_phone_number(n):
    n = ''.join([str(i) for i in n])
    return f"({n[:3]}) {n[3:6]}-{n[6:]}"


"""Best practices
-----------------

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

-----------------

def create_phone_number(n):
    n = ''.join(map(str, n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

-----------------

def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])

  return '({}) {}-{}'.format(str1, str2, str3)

-----------------

def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)
    
-----------------

create_phone_number = lambda n: f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

-----------------
"""

# https://www.codewars.com/kata/reviews/59b1a938182024506b00081d/groups/6355a0dc07f007000186e777
