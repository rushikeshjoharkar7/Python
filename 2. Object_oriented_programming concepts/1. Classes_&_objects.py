"""
Object is a real world entity
Classes can used to create objects
"""


########################################################################
# creating and accessing class using objects

class Bike:  # created class with name "Bike"
    wheels = 2  # variable

    def start_bike(self):  # created a method
        print("Bike started")

    def stop_bike(self):
        print("Bike stopped")


Bike()  # object creation statement
GT_650 = Bike()  # first object (assigning a object to a variable)

print(GT_650.wheels)  # access class variable
GT_650.start_bike()  # access class method

"""
o/p:
2
Bike started
"""

Classic350 = Bike()  # second object

print(Classic350.wheels)  # access class variable
Classic350.stop_bike()  # access class method

"""
o/p:
2
Bike stopped
"""

########################################################################
