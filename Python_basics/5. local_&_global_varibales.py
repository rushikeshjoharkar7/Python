

name = "Shree Ram"                 # Global variable created outside function and can be accessed inside and outside functions


def my_function():
    name = "Jai Mahakal"             # created a local variable with same variable name as global var.
    global name_3                    # created a global variable
    name_2 = "Rushikesh Joharkar"    # this is local variable created inside function and can't be accessed outside the function
    name_3 = "Shree Krishna"         # assigned value to created global variable and this can access both inside and outside function

    print(name)                     # inside function this will print oly local varibale
    print(name_2)
    print(name_3)


my_function()
print("\n")
print(name)
print(name_3)

'''
o/p:
Jai Mahakal
Rushikesh Joharkar
Shree Krishna


Shree Ram
Shree Krishna
'''

##################################################################

# how to update the global variable using a function

name = "Shree Ram"                 # Global variable created outside function and can be accessed inside and outside functions


def my_function():
    global name                     # stated name as a global variable to the function
    name = "Jai Mahakal"            # updated the global variable value
    print(name)                     # inside function this will print oly local variable


my_function()
print(name)

'''
o/p:
Jai Mahakal
Jai Mahakal
'''
