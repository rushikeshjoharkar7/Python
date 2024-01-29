# purpose of functions

# Repetition of code can be avoided using functions
# we can create multiple functions in same python file
#################################################

# function is a block of code
# naming convention of function is same as of variables(snake case)

def my_first_function():  # funtion calling statement
    print("Inside my first function")


# calling the created function, we can call function many number of times
my_first_function()

'''
o/p:
Inside my first function
'''


#################################################

# Parameterizing functions

def print_name(name):  # funtion calling statement with parameter "name"
    print("Your name is: " + name)


print_name("Rushikesh")  # here "Rushikesh" is an argument
print_name("Joharkar")  # here "Joharkar" is an argument

"""
o/p:
Your name is: Rushikesh
Your name is: Joharkar
"""


################################################

# Default arguments in functions
def print_name(name="Shree Ram"):  # funtion calling statement with parameter "name"
    print("Your name is: " + name)


print_name("Rushikesh")  # here "Rushikesh" is an argument
print_name()  # here default argument is considered

"""
o/p:
Your name is: Rushikesh
Your name is: Shree Ram
"""


################################################

# function with multiple parameters

def sum(a, b, c, d):
    print(a + b + c + d)


sum(3, 2, 5, 1)

"""
o/p:
11
"""


################################################

# functions can return data

def sum(a, b):
    return a * b


c = sum(5, 4)
print(c)  # you can directly write as print(sum(5,4))

'''
o/p:
20
'''

################################################
