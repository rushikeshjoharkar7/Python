"""
Method Overloading :
- Method overloading occurs when a class has multiple methods with the same name but
    different parameters (number, type, or order).

- In method overloading, the return type may or may not be different, but the method name
    must be the same.

- Method overloading allows a class to have multiple methods with the same name but
    different behaviors based on the parameters passed to them.

- Method overloading is a compile-time polymorphism concept where the decision
    about which method to call is made by the compiler based on the arguments provided.

- Overloading methods is not directly supported by python.
- Alternative way for method overloading in python is here in this file:
"""


class A:

    def sample(self, a=None, b=None):
        if a != None and b != None:
            print(a * b)
        elif a != None:
            print(a)
        else:
            print("Nothing")


obj = A()
obj.sample(5, 4)
obj.sample(3)
obj.sample()

"""
o/p:
20
3
Nothing
"""
