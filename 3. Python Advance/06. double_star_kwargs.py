"""
*args can be used to pass any number of single values as arguments

**kwargs can be used to pass any number of key-value pairs as arguments
"""


##################################################################################
# *args is used as:

def sample(*p):
    for i in p:
        print(i)


sample(1134, 235, 125, 2135, "werwtat")

"""
o/p:
1134
235
125
2135
werwtat
"""


################################################
#  **kwargs can be used to get key-value pairs as :


def sample(**k):
    for i in k.items():
        print(i)


sample(name="Rushikesh",
       exp=2,
       location="Pune")

"""
o/p:
('name', 'Rushikesh')
('exp', 2)
('location', 'Pune')
"""


####################################################################################
#  **kwargs can be used to get values as :


def sample(**k):
    for i in k.keys():
        print(i)


sample(name="Rushikesh",
       exp=2,
       location="Pune")

"""
o/p:
name
exp
location
"""


####################################################################################
#  **kwargs can be used to get values as :


def sample(**k):
    for i in k.values():
        print(i)


sample(name="Rushikesh",
       exp=2,
       location="Pune")

"""
o/p:
Rushikesh
2
Pune
"""


####################################################################################
#  **kwargs can be used to get key-value pairs as :


def sample(**k):
    for i, j in k.items():
        print(i, j)


sample(name="Rushikesh",
       exp=2,
       location="Pune")

"""
o/p:
name Rushikesh
exp 2
location Pune
"""


####################################################################################
# we can use **kwargs while calling the function by passing the dict as **kwargs

def sample(name, exp, location):
    print(name, exp, location)


d = {"name": "Rushikesh", "exp": 2, "location": "Pune"}

sample(**d)

"""
o/p:
Rushikesh 2 Pune
"""
####################################################################################


