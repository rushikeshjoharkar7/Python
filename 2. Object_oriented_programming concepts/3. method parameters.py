"""
We can use self keyword in python to differentiate class variables and method parameters
"""


#############################################################################################

class Bike:
    wheels = 2

    def sample(self, brand, model, price, mileage):
        print(brand, model, price, mileage)  # method parameters can print here as it is inside same method
        self.brand = brand  # created a class level variable and assign method parameters to it
        self.model = model
        self.price = price
        self.mileage = mileage

    def sample2(self):
        print(self.wheels)   # can access variable within class using "self"
        print(self.brand, self.model, self.price, self.mileage)  # accessing the created class level variables


bike1 = Bike()
bike1.sample("RI", "GT_650", 350000, 30)
bike1.sample2()

"""
o/p:
RI GT_650 350000 30
2
RI GT_650 350000 30
"""
