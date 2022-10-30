"""
@File    : Polish alphabet.py 
@Author  : Richie Black
@Time    : 30.10.2022 23:31

I have been learning Python since August 2022.
"""


def correct_polish_letters(st):
    """There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants.

    Your task is to change the letters with diacritics,
    and print out the string without the use of the Polish letters.
    """
    polish_letters = {
        'ą': 'a', 'ć': 'c', 'ę': 'e',
        'ł': 'l', 'ń': 'n', 'ó': 'o',
        'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    result = ''

    for i in range(len(list(st))):

        if st[i] in polish_letters:
            entry = st[i]
            result += polish_letters[entry]
        else:
            result += st[i]

    print(result)
    return result


"""Best practices
-----------------

def correct_polish_letters(s):
    return s.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))


-----------------

def correct_polish_letters(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i], lt[i])
    return st

-----------------

def correct_polish_letters(st): 
    d={'ą':'a',
    'ć':'c',
    'ę':'e',
    'ł':'l',
    'ń':'n',
    'ó':'o',
    'ś':'s',
    'ź':'z',
    'ż':'z'}
    return "".join(d[c] if c in d else c for c in st)

-----------------
"""

# https://www.codewars.com/kata/reviews/5e859a348be5490001f0692a/groups/634de03c43ed6a0001fe89bd
