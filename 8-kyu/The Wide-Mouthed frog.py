# https://www.codewars.com/kata/reviews/57ec923701c9e93a6000009b/groups/622f6fac2524f50001472ccb

def mouth_size(animal):
    return 'small' if "alligator" in animal.lower() else 'wide'


# I have been studying Python for one month.

"""Best practices
-----------------

def mouth_size(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'

-----------------

def mouth_size(animal):
    mouth = {'alligator':'small'}
    return mouth.get(animal.lower(), 'wide')

-----------------

mouth_size = lambda animal: ["wide","small"][animal.lower()=="alligator"]

-----------------
"""
