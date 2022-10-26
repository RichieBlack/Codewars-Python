"""
@File    : Sleigh Authentication.py 
@Author  : Richie Black
@Time    : 26.10.2022 23:27

I have been learning Python since August 2022.
"""


class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'


"""Best practices
-----------------

class Sleigh(object):
    def authenticate(self, name, password):
        return name == 'Santa Claus' and password == 'Ho Ho Ho!'

-----------------

import hashlib, uuid


class Sleigh(object):
    def __init__(self):
        self.salt = "39d1656331274e45aed30343739ef89b"
        self.enc_password = "45f44255f8b7ac2804a5e008812381297829f64421b69de9c5df0bdc492dab30660ddc\
                             67bd3a7cb4c0f3b91eca229131c72abaedb54d8716dc32160d06725879"
        self.username = "Santa Claus"

    def authenticate(self, name, password):
        return name == self.username and hashlib.sha512(password + self.salt).hexdigest() == self.enc_password   

-----------------

class Sleigh(object):
    def authenticate(self, name, password):
        return (name, password) == ('Santa Claus', 'Ho Ho Ho!')

-----------------

class Sleigh(object):

    def __init__(self):
        self.known_credentials = {'Santa Claus': 'Ho Ho Ho!'}
        
    def authenticate(self, name, password):
        if name in self.known_credentials.keys() and \
          password == self.known_credentials.get(name):
            return True
        else:
            return False
            
-----------------
"""

# https://www.codewars.com/kata/reviews/54a5be7674ff01d7da000063/groups/632f25c91900890001d40d53
