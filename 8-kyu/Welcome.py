"""
@File    : Welcome.py 
@Author  : Richie Black
@Time    : 20.10.2022 20:29

I have been learning Python since August 2022.
"""

greets = {
    'english': 'Welcome',
    'czech': 'Vitejte',
    'danish': 'Velkomst',
    'dutch': 'Welkom',
    'estonian': 'Tere tulemast',
    'finnish': 'Tervetuloa',
    'flemish': 'Welgekomen',
    'french': 'Bienvenue',
    'german': 'Willkommen',
    'irish': 'Failte',
    'italian': 'Benvenuto',
    'latvian': 'Gaidits',
    'lithuanian': 'Laukiamas',
    'polish': 'Witamy',
    'spanish': 'Bienvenido',
    'swedish': 'Valkommen',
    'welsh': 'Croeso'
}


def greet(language):
    return greets[language] if language in greets else 'Welcome'


"""Best practices
-----------------

def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')

-----------------

db = {
'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'}

def greet(language):
    return db.get(language, "Welcome")

-----------------

def greet(language):
  if language=='english':
    return('Welcome')
  elif language=='czech':
    return('Vitejte')
  elif language=='danish':
    return('Velkomst')
  elif language=='dutch':
    return ('Welkom')
  elif language=='estonian':
    return('Tere tulemast')
  elif language=='finnish':
    return('Tervetuloa')
  elif language=='flemish':
    return('Welgekomen')
  elif language=='french':
    return('Bienvenue')
  elif language=='german':
    return('Willkommen')
  elif language=='irish':
    return('Failte')
  elif language=='italian':
    return('Benvenuto')
  elif language=='latvian':
    return ('Gaidits')
  elif language=='lithuanian':
    return ('Laukiamas')
  elif language=='polish':
    return ('Witamy')
  elif language=='spanish':
    return('Bienvenido')
  elif language=='swedish':
    return('Valkommen')
  elif language=='welsh':
    return('Croeso')
  else:
    return('Welcome')

-----------------
"""

# https://www.codewars.com/kata/reviews/578408e3b7bca53e6d000200/groups/63278321921e140001ab60e3
