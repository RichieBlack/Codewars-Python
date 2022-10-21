"""
@File    : All Star Code Challenge 18.py 
@Author  : Richie Black
@Time    : 21.10.2022 21:50

I have been learning Python since August 2022.
"""


def str_count(string, letter):
    return string.count(letter)


"""Best practices
-----------------

def strCount(string, letter):
    return string.count(letter)

-----------------

strCount = str.count

-----------------

def str_count(strng, letter):
    counter = 0
    
    for chr in strng:
        if chr == letter:
            counter += 1
        
    return counter

-----------------

def str_count(strng, letter):
    return (strng.count(letter))
    
-----------------
"""

# https://www.codewars.com/kata/reviews/58683cf4e4604f93660003ed/groups/6329bb1bf5f54000010c5377
