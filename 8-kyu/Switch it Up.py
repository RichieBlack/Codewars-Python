"""
@File    : Switch it Up.py 
@Author  : Richie Black
@Time    : 20.10.2022 21:38

I have been learning Python since August 2022.
"""


def switch_it_up(number):
    return {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }[number]


"""Best practices
-----------------

def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]

-----------------

def switch_it_up(number):
    number_converter={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    return number_converter[number]

-----------------

def switch_it_up(number):
    dict = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"}
    
    return dict.get(number)

-----------------
"""

# https://www.codewars.com/kata/reviews/580cfb2092a920b4b2000013/groups/63284a77a9ebca0001d338b4
