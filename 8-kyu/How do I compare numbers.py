def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


# I have been studying Python for two months.

'''
Best practices
--------------

def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

--------------

def what_is(x):
  return { 42: 'everything', 1764: 'everything squared' }.get(x, 'nothing')

--------------
'''
