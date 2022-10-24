"""
@File    : Stop gninnipS My sdroW.py 
@Author  : Richie Black
@Time    : 24.10.2022 19:26

I have been learning Python since August 2022.
"""


def spin_words(sentence):
    return " ".join([i if len(i) < 5 else i[::-1] for i in sentence.split()])


"""Best practices
-----------------

def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

-----------------

def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

-----------------

def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string

-----------------

def spin_words(sentence):
    return ' '.join(word if len(word) < 5 else word[::-1] for word in sentence.split())

-----------------
"""

# https://www.codewars.com/kata/reviews/55401901b8a14241e4000048/groups/6356b8b657b4a500015c4f9f
