"""
Abstraction in Python - Abstract Classes and Abstract Methods

- For partial implementation of Class, we can use Abstract classes
- When what to implement is clear but how to implement is not clear then we have to go for
   Abstract classes and Abstract methods.

Abstract Methods - Methods which are just defined but without implementation or method body.
Abstract Classes - Classes having at least one abstract method

- We can't directly create objects for Abstract Classes, we have to create the child class
   which implement the parent class
"""
#####################################################################################################

from abc import ABC, abstractmethod  # ABC is predefined abstract class


# Abstract Class - Partial implementation
class A(ABC):

    # Abstract Method
    @abstractmethod
    def method_one(self):
        pass

    # Abstract Method
    @abstractmethod
    def method_two(self):
        pass

    # Non-Abstract Method
    def method_three(self):
        print("Inside method three")

# as we can't create a object for abstract class, we need to create child class


class B(A):

    def method_one(self):
        print("Inside Method one")

    def method_two(self):
        print("Inside method two")

    
b = B()
b.method_three()
b.method_one()
b.method_two()

"""
o/p:
Inside method three
Inside Method one
Inside method two
"""
####################################################################################################################

# if we don't implement all methods of abstract class in child class, then child class also becomes abstract class

from abc import ABC, abstractmethod  # ABC is predefined abstract class


# Abstract Class - Partial implementation
class A(ABC):

    # Abstract Method
    @abstractmethod
    def method_one(self):
        pass

    # Abstract Method
    @abstractmethod
    def method_two(self):
        pass

    # Non-Abstract Method
    def method_three(self):
        print("Inside method three")


# as we can't create a object for abstract class, we need to create child class


class B(A):

    def method_one(self):
        print("Inside Method one")


class C(B):

    def method_two(self):
        print("Inside method two")


c = C()
c.method_three()
c.method_one()
c.method_two()

"""
o/p:
Inside method three
Inside Method one
Inside method two
"""
#####################################################################################################

# Constructor can be created inside the Abstract Class for initializing the variables

from abc import ABC, abstractmethod  # ABC is predefined abstract class


# Abstract Class - Partial implementation
class A(ABC):

    def __init__(self, a):
        self.a = a

    # Abstract Method
    @abstractmethod
    def method_one(self):
        pass

    # Abstract Method
    @abstractmethod
    def method_two(self):
        pass

    # Non-Abstract Method
    def method_three(self):
        print("Inside method three, ", self.a)


# as we can't create a object for abstract class, we need to create child class


class B(A):

    def method_one(self):
        print("Inside Method one")


class C(B):

    def method_two(self):
        print("Inside method two")


c = C(1000000)
c.method_three()
c.method_one()
c.method_two()

"""
o/p:
Inside method three,  1000000
Inside Method one
Inside method two
"""

#####################################################################################################
