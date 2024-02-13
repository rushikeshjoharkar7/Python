"""
*args is a function parameter which can receive any number of arguments

we can give any name at "args"
"""


def sample(*args):
    for i in args:
        print(i)


sample(12, 4134, 14)  # can accept more than one arguments
"""
o/p:
12
4134
14
"""


######################################################################################
# we can give any name at "args"


def sample(*abc):
    for i in abc:
        print(i)


sample(12, "afga", "awegg")  # can accept more than one arguments

"""
o/p:
12
afga
awegg
"""


######################################################################################
# we can use *args while calling the function by passing the list of values as *args


def sample(a, b, c, d):
    print(a, b, c, d)


args = [2134, 235, 365, "sgg"]
sample(*args)

"""
o/p:
2134 235 365 sgg
"""
######################################################################################
