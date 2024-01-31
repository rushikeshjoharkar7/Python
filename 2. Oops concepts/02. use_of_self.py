"""
To use class properties within class, we need to use "self"
"""


class Bike:  # created class with name "Bike"
    wheels = 2  # variable

    def start_bike(self):
        print("Bike started")

    def example_one(self):
        print(self.wheels)          # to use class properties within class, we need to use "self"
        self.start_bike()           # to use class properties within class, we need to use "self"


# Using object reference, we can access the properties of class outside the class
bike1 = Bike()
print(bike1.wheels)
bike1.start_bike()
bike1.example_one()

"""
o/p:
2
Bike started
2
Bike started
"""