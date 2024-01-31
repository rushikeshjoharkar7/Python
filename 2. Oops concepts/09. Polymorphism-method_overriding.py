"""
- Method overriding occurs when a subclass provides a specific implementation of
    a method that is already provided by one of its parent classes.
"""


class A:

    a = 5

    def sample(self):
        print("Inside sample method of Class A")


class B(A):

    a = 10     # override the variable value of value in class A

    def sample(self):           # same method name as like in class A and it overrides method properties of class A
        print("Inside sample method of Class B")


obj = B()
print(obj.a)
obj.sample()

obj2 = A()
print(obj2.a)
obj2.sample()

"""
o/p:
10
Inside sample method of Class B
5
Inside sample method of Class A
"""