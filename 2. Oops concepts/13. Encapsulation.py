"""
Encapsulation is a mechanism, which wraps the data (i.e. variables) and code (i.e. methods)
together under a single unit(i.e. class)

- in encapsulation, you cannot access data(i.e.variables) as a single unit, instead we have to
take the help of methods to access the data(i.e.variables)

- Encapsulation is achieved by privatizing the variables and accessing them by using getters
and setters methods to modify and get the variable values.

- Binding the data to the class by making the variables as private and accessing them only
via non-private methods(getter and setter methods).
"""
#######################################################################################################


class A:

    __age = 0       # private variable

    def set_age(self, age):      # setter method (non-private method)
        A.__age = age       # setting the private variable in setter method's variable

    def get_age(self):      # getter method (non-private method)
        return A.__age      # getting the private variable as return in getter method's variable


obj = A()
obj.set_age(45)         # value of a is modified with 45
print(obj.get_age())

"""
o/p:
45
"""
