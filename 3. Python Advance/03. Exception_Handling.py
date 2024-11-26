"""
Exception Handling in Python:

- We get exceptions in python due to invalid input to the program
"""
################################################################################
# when we don't follow exception handling
# After error comes, no further code will execute

print("start program")
a = 10/0
print(a)
print("stop program")

"""
o/p:
    a = 10/0
ZeroDivisionError: division by zero
start program
"""
################################################################################
x = 5
y = "hello"
try:
    z = x + y
except Exception as e:
    print("Error: ", e)
##################################################################################
try:
    result = 10 / 0  

except Exception as e:
    print("An error occurred:", e)
###############################################################################
# with exception handling

print("start program")

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError:
    print("Exception got handled")

print("start program")

"""
o/p:
start program
Exception got handled
stop program
"""
##############################################
# for detailed exception 

print("start program")

try:
    a = 10 / 0
    print(a)
except ZeroDivisionError as m:
    print("Exception got handled: ",m)

print("End program")

"""
o/p:
start program
Exception got handled:  division by zero
End program
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
"""
"""
o/p_2:
start program
enter a number: 0
Exception got handled
stop program
"""
#################################################################################
# Type Error

print("Start code")
print("enter ur input: ")
a=input()

try:
    b = 10+a
except TypeError:
    print("Exception got handled")

print("End code")

"""
o/p:
Start code
enter ur input: 
g
Exception got handled
End code
"""
#################################################################################
# Name Error

print("Start code")

try:
    print(a)
except NameError:
    print("Exception got handled")

print("End code")

"""
o/p:
Start code
Exception got handled
End code
"""
################################################
# for detailed exception 

print("Start code")

try:
    print(a)
except NameError as n:
    print("Exception got handled: ", n)

print("End code")

"""
o/p:
Start code
Exception got handled:  name 'a' is not defined
End code
"""
#################################################################################
# try, except, else and finally

print("start program")

try:
    a = 10 / 1
    print(a)

except ZeroDivisionError as m:
    print("Exception got handled: ",m)
except NameError as n:
    print("Exception got handled: ", n)
except TypeError as t:
    print("Exception got handled: ", t)

# when exception is not execute then else bloc will be executed
else:
    print("Inside else block")

# no matter exception block executes or not, finally block will execute always
finally:
    print("Inside finally block")

print("End program")

"""
o/p:
start program
10.0
Inside else block becoz exception is not thrown
Inside finally block
End program
"""
##################################################

print("start program")

try:
    a = 10 / 0
    print(a)

except ZeroDivisionError as m:
    print("Exception got handled: ",m)
except NameError as n:
    print("Exception got handled: ", n)
except TypeError as t:
    print("Exception got handled: ", t)

# when exception is not execute then else bloc will be executed
else:
    print("Inside else block")

# no matter exception block executes or not, finally block will execute always
finally:
    print("Inside finally block")

print("End program")

"""
o/p:
start program
Exception got handled:  division by zero
Inside finally block
End program
"""
################################################################################

# raise a customized exception

print("start program")
print("Input your child's age:")
age = int(input())

try:
    if age<5:
        raise ValueError("Below 5 years of age is not eligible")
    else:
        print("Child is eligible")

except ValueError as v:
    print("Exception got handled:",v)


print("End program")

"""
o/p:
start program
Input your child's age:
2
Exception got handled: Below 5 years of age is not eligible
End program
"""
################################################################################










