"""
super():
    - Accessing or calling the parent class properties (variables and methods) from child class,
      which are having the same name as child class properties.

    - If the child class doesn't have any constructor and the parent class has a constructor,
      it will be automatically invoked on creating an object for child class.

    - But if the child class has its own constructor, then the parent class constructor won't be
      invoked and we have to call it explicitly from child class constructor using super().
"""
############################################################################################################
# There are two uses of super()
# 1. for accessing the parent class properties


class A:

    a = 5

    def sample(self):
        print("Inside sample method of class A")


class B(A):     # single inheritance

    a = 10

    def sample(self):
        print("Inside sample method of class B")

    def print_properties(self):
        
        print(self.a)       # accessing overridden value of a
        print(super().a)    # accessing the parent class value of a

        self.sample()       # accessing overridden method
        super().sample()    # accessing the parent class method


obj = B()
obj.print_properties()

"""
o/p:
10
5
Inside sample method of class B
Inside sample method of class A
"""
############################################################################################################

# 2. Call the __init__ method of parent class


class A:
    def __init__(self):
        print("Inside __init__ method of Class A")


class B(A):  # single inheritance
    def __init__(self):
        super().__init__()      # calling parent class A's __init__ method from child class B
        print("Inside __init__ method of Class B")


B()

"""
o/p:
Inside __init__ method of Class A
Inside __init__ method of Class B
"""

############################################################################################################
