# link: https://www.codewars.com/kata/reviews/55286b1c6e62d34b78000177/groups/5ffe243b06e2ef0001cb1a74

def reverse_words(s):
    return " ".join(w for w in s.split(" ")[::-1])

'''
Best practices
--------------

def reverseWords(str):
    return " ".join(str.split(" ")[::-1])

--------------

def reverseWords(str):
    return ' '.join(reversed(str.split()))

--------------

reverseWords = lambda _:' '.join(_.split()[::-1])

--------------
'''