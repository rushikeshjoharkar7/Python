"""
We can not access private properties of a class outside the class.
"""


class A:

    __a = 5     # private variable

    def __sample(self):     # private method
        print("Inside sample method of class A")

    def print_details(self):
        print(self.__a)     # can access private variables inside class only
        self.__sample()     # can access private methods inside class only


obj = A()

obj.print_details()     # this is way to access private properties outside the class


"""
o/p:
5
Inside sample method of class A
"""

#########################################################################################################

"""
Getter and setter non-private methods can be used for accessing the private variables
"""


class A:

    __age = 0       # private variable

    def set_age(self, age):      # setter method (non-private method)
        A.__age = age       # setting the private variable in setter method's variable

    def get_age(self):      # getter method (non-private method)
        return A.__age      # getting the private variable as return in getter method's variable


obj = A()
obj.set_age(45)         # value of a is modified with 14
print(obj.get_age())


"""
o/p:
45
"""