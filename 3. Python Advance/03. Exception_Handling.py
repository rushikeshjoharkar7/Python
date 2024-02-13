"""
Exception Handling in Python:

- We get exceptions in python due to invalid input to the program
"""
################################################################################
# when we don't follow exception handling
# After error comes, no further code will execute
"""
print("start program")
a = 10/0
print(a)
print("stop program")


o/p:
    a = 10/0
ZeroDivisionError: division by zero
start program

################################################################################

# with exception handling

print("start program")

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Exception got handled")

print("start program")


o/p:
start program
Exception got handled
stop program
"""

################################################################################

print("start program")
num = int(input("enter a number: "))

try:
    a = 10 / num
    print(a)
except ZeroDivisionError:
    print("Exception got handled")

print("stop program")

"""
o/p_1:
start program
enter a number: 100
0.1
stop program

o/p_2:
start program
enter a number: 0
Exception got handled
stop program
"""