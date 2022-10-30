"""
@File    : Man in the west.py 
@Author  : Richie Black
@Time    : 30.10.2022 15:00

I have been learning Python since August 2022.
"""


def check_the_bucket(bucket):
    match bucket:
        case (*_, ) if 'gold' in bucket:
            return True
        case other:
            return False


"""Best practices
-----------------

def check_the_bucket(bucket):
    return 'gold' in bucket

-----------------

def check_the_bucket(bucket):
    if "gold" in bucket:

        return True

    else:

        return False

-----------------

check_the_bucket = lambda bucket: 'gold' in bucket

-----------------
"""

# https://www.codewars.com/kata/reviews/59bd6595a0640efb51002227/groups/6345c37c2d0c58000132ea74
