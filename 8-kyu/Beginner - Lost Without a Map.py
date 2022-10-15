# link: https://www.codewars.com/kata/reviews/57fbf74b777d18094c0000e4/groups/5de2e4ba73689000016f9a93

def maps(a):
    double = []
    for i in a:
        i = i * 2
        double.append(i)
    return double


'''
Best practices
--------------

def maps(a):
    return [2 * x for x in a]

--------------

def maps(a):
    return map(lambda x: 2 * x, a)

--------------

maps = lambda a:[n * 2 for n in a]

--------------
'''
