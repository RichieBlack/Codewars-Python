"""
@File    : CSV representation of array.py 
@Author  : Richie Black
@Time    : 06.11.2022 21:34

I have been learning Python since August 2022.
"""


def to_csv_text(array):
    output = []

    for i in array[:-1]:
        output.append(i)
        i.append("\n")

    output += array[-1:]

    output2 = []
    for j in output:
        output2.extend(j)

    b = ",".join(map(str, output2))

    return b.replace(',\n,', '\n')


def to_csv_text_alt(array):
    new_string = "\n".join(map(str, array))
    return (new_string.replace(" ", "").replace("[", "").replace("]", ""))


"""Best practices
-----------------

def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)

-----------------

def toCsvText(array) :
   return '\n'.join(','.join(str(n) for n in lst) for lst in array)

-----------------

def toCsvText(array) :
    return(str(array).replace('],', '\n').replace('[', '').replace(']', '').replace(' ', ''))   

-----------------
"""

# https://www.codewars.com/kata/reviews/5a83d0bb013374df9a000406/groups/63692e52a761d100012437ec
